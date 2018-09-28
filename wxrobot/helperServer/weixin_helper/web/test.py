# -*- coding: utf-8 -*-

from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet import reactor

from common import common_setting
from common.common_setting import helper_dict
from common.server_base.decorate_base import msg_resolver
from common.server_base.wx_hub_linker_protocal import HubLinkerProtocol
from common.thrift.body.ttypes import HelperLoginReq, SendMessageReq, AddFriendQRReq, OpenGroupReq, ServerHeartbeatResp
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

    @msg_resolver(AppId.AppType_ServerSystem, FunctionId.ServerSystemHeartbeat, ServerHeartbeatResp)
    def on_heartbeat(self, msg):
        from datetime import datetime
        self.last_heartbeat_time = datetime.now()
        # smart_log('收到hub心跳返回')


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

