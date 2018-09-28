# -*- coding: utf-8 -*-
from datetime import datetime

from twisted.internet.protocol import ServerFactory
from twisted.internet.task import LoopingCall
from twisted.internet import endpoints, reactor

import uuid

from common import common_setting
from common.redis.helper_session import HelperSession
from common.server_base.decorate_base import msg_resolver
from common.server_base.wx_msg_base_protocal import WxMsgBaseProtocal
from common.thrift.body.ttypes import ServerHeartbeatReq, ServerHeartbeatResp, ServiceRegisterReq, ServiceRegisterResp, \
    ResponseInfo
from common.thrift.define.ttypes import AppId, FunctionId, DirectionType, ResponseCode
from common.thrift.head.ttypes import WxHead
from common.utils.logger import start_twisted_logging, smart_log

__author__ = 'jerry'

CHECK_INTERVAL = 15.0
HEARTBEAT_MAX_INTERVAL = 15.0 * 3
APP_SESSION_TIME_OUT = 60 * 10
WEB_SESSION_TIME_OUT = 60 * 15
SESSION_CHECK_INTERVAL = 60

all_node_list = []
helper_service_dict = {}  # 格式 {"server_token":{"payload":0, "protocal":serverProtocal}}
web_service_dict = {}  # 格式 {"server_token":{"payload":0, "protocal":serverProtocal}}
subscribe_dict = {}


class HubProtocal(WxMsgBaseProtocal):
    service_id = None
    last_heartbeat_time = None
    server_token_id = None

    # is_gateway = False
    # is_active = False

    @msg_resolver(AppId.AppType_ServerSystem, FunctionId.ServerSystemHeartbeat, ServerHeartbeatReq)
    def on_hub_heartbeat(self, msg):
        self.last_heartbeat_time = datetime.now()
        smart_log("心跳 app_id:%d server_token:%s" % (self.service_id, self.server_token_id))
        head = WxHead()
        head.appId = AppId.AppType_ServerSystem
        head.functionId = FunctionId.ServerSystemHeartbeat
        head.direction = DirectionType.ToWxServer
        resp = ServerHeartbeatResp()
        resp.response = ResponseInfo(code=ResponseCode.Succeed)
        self.send_msg(head=head, body=resp)

        # 更新负载
        if msg.body.payloadCount:
            if msg.head.appId == AppId.AppType_HelperServer and helper_service_dict[msg.head.serverTokenId]:
                helper_service_dict[msg.head.serverTokenId]["payload"] = msg.body.payloadCount
            elif msg.head.appId == AppId.AppType_WebServer and web_service_dict[msg.head.serverTokenId]:
                web_service_dict[msg.head.serverTokenId]["payload"] = msg.body.payloadCount

    @msg_resolver(AppId.AppType_ServerSystem, FunctionId.ServerSystemServiceRegister, ServiceRegisterReq)
    def on_hub_service_register(self, msg):
        smart_log("注册:")

        # 产生服务器的唯一标识 如果服务器注册过 则使用之前的
        if msg.head.serverTokenId and len(msg.head.serverTokenId) > 0:
            server_token_id = msg.head.serverTokenId
        else:
            server_token_id = str(uuid.uuid1())

        self.server_token_id = server_token_id
        self.service_id = msg.body.serviceAppId

        head = WxHead()
        head.appId = AppId.AppType_ServerSystem
        head.functionId = FunctionId.ServerSystemServiceRegister

        if msg.body.serviceAppId == AppId.AppType_HelperServer:
            print("WxHelperServer 注册到Hub")
            helper_service_dict[server_token_id] = {"payload": 0, "protocal": self}
            head.direction = DirectionType.ToWxServer
        elif msg.body.serviceAppId == AppId.AppType_WebServer:
            print("WebServer 注册到Hub")
            web_service_dict[server_token_id] = {"payload": 0, "protocal": self}
            head.direction = DirectionType.ToWebServer

        # if msg.body.serviceAppId:
        #     smart_log("注册服务 app_id:%d server_token:%s" % (self.service_id, self.server_token_id))
        #     for sub_id in msg.body.subScribeFunctionId:
        #         if sub_id not in subscribe_dict:
        #             subscribe_dict[sub_id] = []
        #         if self not in subscribe_dict[sub_id]:
        #             subscribe_dict[sub_id].append(self)
        #             smart_log("添加订阅 app_id:%d server_token:%s" % (self.service_id, self.server_token_id))

        resp = ServiceRegisterResp()
        resp.response = ResponseInfo(code=ResponseCode.Succeed)
        resp.serverTokenId = server_token_id

        self.send_msg(head=head, body=resp)

    def remove_from_container(self):
        smart_log("移除节点 app_id:%d server_token:%s" % (self.service_id, self.server_token_id))
        if self in all_node_list:
            all_node_list.remove(self)

        if self.server_token_id:
            if self.service_id == AppId.AppType_HelperServer:
                del helper_service_dict[self.server_token_id]
            elif self.service_id == AppId.AppType_WebServer:
                del web_service_dict[self.server_token_id]
                # for k, v in subscribe_dict.items():
                #     if self in v:
                #         v.remove(self)

    def unresolve_msg(self, msg):
        # 转发消息
        smart_log('收到消息\r\n %s' % msg.head)
        if msg.head.direction == DirectionType.ToWebServer:
            print("转发Web服务的数据包: {}".format(msg))
            if msg.head.tag == 2 and msg.head.serverTokenId and web_service_dict[msg.head.serverTokenId]:
                # 为某个请求的返回, 并且需要原路返回
                web_service_dict[msg.head.serverTokenId]["protocal"].send_msg(msg=msg, use_raw_buf=True)
            else:
                optimal_protocal = None
                min_payload = None
                for server_token, web_server in web_service_dict.items():
                    if not min_payload:
                        min_payload = web_server["payload"]
                        optimal_protocal = web_server["protocal"]
                    if min_payload > web_server["payload"]:
                        min_payload = web_server["payload"]
                        optimal_protocal = web_server["protocal"]
                if optimal_protocal:
                    optimal_protocal.send_msg(msg=msg, use_raw_buf=True)

        elif msg.head.direction == DirectionType.ToWxServer:
            print("转发助手服务的数据包: {}".format(msg))
            if msg.head.helperToken:
                # 获取助手指定的wx_helper_server
                helper_session = HelperSession(helper_token=msg.head.helperToken, helper_server_token=None)
                helper_session.get_server_token_by_helper_token()
                helper_server_token = helper_session.helper_server_token
                if helper_server_token and helper_service_dict.get(helper_server_token.decode()):
                    print("指定助手转发助手服务的数据包: {}".format(msg))
                    helper_service_dict.get(helper_server_token.decode())["protocal"].send_msg(msg=msg, use_raw_buf=True)
                else:
                    # TODO 指定服务出现异常
                    smart_log("指定服务出现异常, helper_server_token:{}, helper_token:{}"
                              .format(helper_server_token, msg.head.helperToken))
                    helper_session.delete_server_relation_by_helper_token()
            else:
                # 未指定相关助手
                optimal_protocal = None
                min_payload = None
                for server_token, helper_server in helper_service_dict.items():
                    if not min_payload:
                        min_payload = helper_server["payload"]
                        optimal_protocal = helper_server["protocal"]
                    if min_payload > helper_server["payload"]:
                        min_payload = helper_server["payload"]
                        optimal_protocal = helper_server["protocal"]
                if optimal_protocal:
                    print("选取最优助手转发助手服务的数据包: {}".format(msg))
                    optimal_protocal.send_msg(msg=msg, use_raw_buf=True)
        else:
            print("未知转发方向的数据包: {}".format(msg))

    def connectionLost(self, reason):
        smart_log('链接断开')
        self.remove_from_container()


class HubFactory(ServerFactory):
    check_task = None

    def doStart(self):
        from twisted.internet.task import LoopingCall

        self.check_task = LoopingCall(self.check_client_heartbeat)
        self.check_task.start(CHECK_INTERVAL)

    def buildProtocol(self, addr):
        print("---->>>>>> 新连接请求 address %s" % addr)
        p = HubProtocal()
        all_node_list.append(p)
        return p

    def doStop(self):
        self.check_task.stop()

    def check_client_heartbeat(self):
        now = datetime.now()
        for client in all_node_list:
            if client.last_heartbeat_time and (now - client.last_heartbeat_time).seconds > HEARTBEAT_MAX_INTERVAL:
                client.remove_from_container()


def clear_timeout_session():
    # TODO
    # MGSession.clear_all_timeout(APP_SESSION_TIME_OUT, WEB_SESSION_TIME_OUT)
    print("定时任务：session清除")


if __name__ == '__main__':
    t = LoopingCall(clear_timeout_session)  # 清除无效session
    t.start(SESSION_CHECK_INTERVAL)
    start_twisted_logging("hub_server")
    endpoints.serverFromString(reactor, common_setting.hub_server_address).listen(HubFactory())
    reactor.run()
