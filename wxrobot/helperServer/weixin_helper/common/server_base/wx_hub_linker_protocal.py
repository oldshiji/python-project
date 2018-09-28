# -*- coding: utf-8 -*-

from twisted.internet.task import LoopingCall
from datetime import datetime

from common.server_base.decorate_base import msg_resolver
from common.server_base.wx_msg_base_protocal import WxMsgBaseProtocal
from common.thrift.body.ttypes import ServerHeartbeatResp, ServiceRegisterResp, ServiceRegisterReq, ServerHeartbeatReq
from common.thrift.define.ttypes import AppId, FunctionId
from common.utils.logger import smart_log

__author__ = 'jerry'

HEARTBEAT_INTERVAL = 15
HEARTBEAT_MAX_INTERVAL = 15.0 * 3


class HubLinkerProtocol(WxMsgBaseProtocal):
    serviceAppId = -1
    serverTokenId = u''
    subScribeFunctionId = []
    task = None
    last_heartbeat_time = None

    def get_server_token_id(self):
        return self.serverTokenId

    @msg_resolver(AppId.AppType_ServerSystem, FunctionId.ServerSystemHeartbeat, ServerHeartbeatResp)
    def on_heartbeat(self, msg):
        self.last_heartbeat_time = datetime.now()
        # smart_log('收到hub心跳返回')

    @msg_resolver(AppId.AppType_ServerSystem, FunctionId.ServerSystemServiceRegister, ServiceRegisterResp)
    def on_service_register(self, msg):
        self.serverTokenId = msg.body.serverTokenId
        smart_log('收到挂载包 name:%s' % self.serverTokenId)
        self.last_heartbeat_time = datetime.now()
        self.task = LoopingCall(self.send_heartbeat)
        self.task.start(HEARTBEAT_INTERVAL)

    def send_link_req(self):
        """
        发送挂载包
        :rtype : None
        """
        body = ServiceRegisterReq()
        body.serviceAppId = self.serviceAppId
        body.subScribeFunctionId.extend(self.subScribeFunctionId)

        self.send_msg_to_hub(app_id=AppId.AppType_ServerSystem, function_id=FunctionId.ServerSystemServiceRegister,
                             body=body, server_token_id=self.serverTokenId)

    def send_heartbeat(self):
        """
        发送心跳包
        :return:
        """
        now = datetime.now()
        if self.last_heartbeat_time and (now - self.last_heartbeat_time).seconds > HEARTBEAT_MAX_INTERVAL:
            print('心跳超时，准备重连')
            smart_log('心跳超时，准备重连')
            self.task.stop()
            self.transport.loseConnection()
            return

        body = ServerHeartbeatReq()
        body.payloadCount = 0

        self.send_msg_to_hub(app_id=AppId.AppType_ServerSystem, function_id=FunctionId.ServerSystemHeartbeat,
                             body=body, server_token_id=self.serverTokenId)

    def connectionMade(self):
        self.send_link_req()
