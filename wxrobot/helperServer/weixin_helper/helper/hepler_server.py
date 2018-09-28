# -*- coding: utf-8 -*-
import codecs
import time

from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet import reactor

from common import common_setting
from common.common_setting import helper_dict
from common.server_base.decorate_base import msg_resolver
from common.server_base.wx_hub_linker_protocal import HubLinkerProtocol
from common.thrift.body.ttypes import HelperLoginReq, SendMessageReq, AddFriendQRReq, OpenGroupReq
from common.thrift.define.ttypes import AppId, FunctionId
from common.utils.logger import smart_log, start_twisted_logging

__author__ = 'jerry'

Wx_Helper_Linker_Protocol = None


# DEFAULT_PAGE_SIZE = 10
# codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
# count = 0


class WxHelperLinkerProtocol(HubLinkerProtocol):
    serviceAppId = AppId.AppType_HelperServer
    subScribeFunctionId = [FunctionId.ServerSystemUserStatusChange]

    @msg_resolver(AppId.AppType_HelperServer, FunctionId.HelperServer_HelperLogin, HelperLoginReq,
                  is_asyn=True)
    def helper_login(self, msg):
        """
        管家登录请求
        :param msg:
        :return:
        """
        smart_log('收到管家登录请求, mark={}'.format(msg.head.mark))
        from helper.wx_hepler import HelperStart
        global Wx_Helper_Linker_Protocol
        helper_thread = HelperStart(mark=msg.head.mark, protocol=Wx_Helper_Linker_Protocol, web_server_token=msg.head.serverTokenId)
        helper_thread.start()

    @msg_resolver(AppId.AppType_HelperServer, FunctionId.HelperServer_SendMessageToWX, SendMessageReq,
                  is_asyn=True)
    def send_message_to_wx(self, msg):
        """
        发送消息到微信
        :param msg:
        :return:
        """
        smart_log('收到发送消息到微信请求')
        helper_token = msg.head.helperToken
        msg_type = msg.body.msgType
        content = msg.body.content
        to_username_list = msg.body.toUserNameList

        wx_helper = helper_dict.get(helper_token)
        if to_username_list and len(to_username_list) > 0:
            for to_username in to_username_list:
                wx_helper.web_wx_send_msg(content, to_username)

    @msg_resolver(AppId.AppType_HelperServer, FunctionId.HelperServer_AddFriendQR, AddFriendQRReq,
                  is_asyn=True)
    def add_friend_qr(self, msg):
        """
        请求添加好友二维码
        :param msg:
        :return:
        """

    @msg_resolver(AppId.AppType_HelperServer, FunctionId.HelperServer_OpenGroup, OpenGroupReq,
                  is_asyn=True)
    def open_group(self, msg):
        """
        开群
        :param msg:
        :return:
        """


class WxHelperLinkerFactory(ReconnectingClientFactory):
    initialDelay = 5.0

    def buildProtocol(self, addr):
        global Wx_Helper_Linker_Protocol
        Wx_Helper_Linker_Protocol = WxHelperLinkerProtocol()
        return Wx_Helper_Linker_Protocol


if __name__ == '__main__':
    start_twisted_logging('wx_helper_server')

    # from helper.thrift_server import ThriftServer
    # ThriftServer().start()

    reactor.connectTCP(common_setting.wx_helper_linker_address[0], common_setting.wx_helper_linker_address[1],
                       WxHelperLinkerFactory())
    reactor.run()
