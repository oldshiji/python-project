# -*- coding: utf-8 -*-
import threading

from twisted.internet.protocol import ReconnectingClientFactory

from twisted.internet import reactor

from common import common_setting
from common.common_setting import qr_code_map
from common.db_model.community_db.community_db_base import community_session_scope
from common.server_base.decorate_base import msg_resolver
from common.server_base.wx_hub_linker_protocal import HubLinkerProtocol
from common.thrift.body.ttypes import HelperLoginResp, SendMessageResp, ReceiveMessageResp, LoginSuccessResp, \
    AddFriendQRResp, SendMessageReq

from common.thrift.define.ttypes import AppId, FunctionId, DirectionType, MsgType
from common.thrift.head.ttypes import WxHead

__author__ = 'liujinren'

WEB_ACCESS_LINKER_PROTOCOL = None


class WebAccessLinkerProtocol(HubLinkerProtocol):
    serviceAppId = AppId.AppType_WebServer

    @msg_resolver(AppId.AppType_WebServer, FunctionId.HelperServer_HelperLogin, HelperLoginResp)
    def helper_login(self, msg):
        """
        请求管家登录返回
        :param msg:
        :return:
        """
        # print("二维码返回: {}".format(msg))
        qr_code_map.setdefault(msg.head.mark, msg.body.qrCodeUrl)

    @msg_resolver(AppId.AppType_WebServer, FunctionId.HelperServer_LoginSuccess, LoginSuccessResp)
    def helper_login(self, msg):
        """
        登录成功返回
        :param msg:
        :return:
        """
        print("登录成功返回: {}".format(msg))
        del qr_code_map[msg.head.mark]

    @msg_resolver(AppId.AppType_HelperServer, FunctionId.HelperServer_SendMessageToWX, SendMessageResp, is_asyn=True)
    def helper_login(self, msg):
        """
        发送消息返回
        :param msg:
        :return:
        """
        print("发送消息返回：")

    @msg_resolver(AppId.AppType_WebServer, FunctionId.HelperServer_ReceiveMessage, ReceiveMessageResp, is_asyn=True)
    def helper_login(self, msg):
        """
        接受微信消息
        :param msg:
        :return:
        """
        # 识别指令  @kayla1 开通此群
        if msg.body.originalContent and str(msg.body.originalContent) == "@" + msg.body.groupShowName + " 开通此群":
            if msg.body.isBuy == 2:  # 此群已开通
                print("发送消息: 此群已开通")
            else:  # 请管理员开通此群, (设置 “我在本群的昵称”)
                # fixme 检查是否有额度
                pass
                # fixme 请管理员开通此群, (设置 “我在本群的昵称”)

    @msg_resolver(AppId.AppType_WebServer, FunctionId.HelperServer_AddFriendQR, AddFriendQRResp, is_asyn=True)
    def helper_login(self, msg):
        """
        添加好友返回
        :param msg:
        :return:
        """

    def send_msg_to_wx_helper(self, open_id, content, group_id_list, msg_type=MsgType.MsgType_Text):
        """
        发送消息给群
        :param msg_type:
        :param open_id:
        :param content:
        :param group_id_list:
        :return:
        """
        with community_session_scope() as session:
            from common.db_model.community_db.customer_info import CustomerInfo
            bool_, customer_info = CustomerInfo.get_customer_info_by_open_id(session=session, open_id=open_id)
            from common.db_model.user_db.group_info import GroupInfo
            group_list = GroupInfo.get_group_list_by_group_id_list(session=session, group_id_list=group_id_list)
        if bool_ and customer_info.HelperToken and group_list:
            head_ = WxHead()
            head_.helperToken = customer_info.HelperToken
            head_.appId = AppId.AppType_HelperServer
            head_.functionId = FunctionId.HelperServer_SendMessageToWX
            head_.direction = DirectionType.ToWxServer
            # 返回指定的web 服务
            head_.tag = 2
            head_.serverTokenId = self.serverTokenId

            req = SendMessageReq()
            req.msgType = int(msg_type)
            req.content = content
            req.toUserNameList = [item.UserName for item in group_list]
            self.send_msg(head=head_, body=req)
        else:
            print("获取用户信息失败")


class WebAccessLinkerFactory(ReconnectingClientFactory):
    initialDelay = 5.0

    def buildProtocol(self, addr):
        self.resetDelay()
        global WEB_ACCESS_LINKER_PROTOCOL
        WEB_ACCESS_LINKER_PROTOCOL = WebAccessLinkerProtocol()
        return WEB_ACCESS_LINKER_PROTOCOL


def web_access_initialize():
    """
    初始化web_access_linker
    :return:
    """

    def start_hub_linker():
        reactor.connectTCP(common_setting.web_access_linker_address[0], common_setting.web_access_linker_address[1],
                           WebAccessLinkerFactory())
        reactor.run(installSignalHandlers=False)

    threading._start_new_thread(start_hub_linker, ())
