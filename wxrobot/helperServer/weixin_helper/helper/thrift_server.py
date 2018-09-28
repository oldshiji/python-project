# -*- coding: utf-8 -*-


import threading
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from common.thrift.body.ttypes import HelperLoginResp
from common.thrift.server import WeiXinHelperService


class WxHelperHandler(WeiXinHelperService.Iface):
    """

    """

    def __init__(self):
        self.log = {}

    def ping(self, clientTime):
        super().ping(clientTime)

    def helperLogin(self, req):
        """
        请求管家登录
        :param req:
        :return:
        """
        super().helperLogin(req)
        resp = HelperLoginResp()
        return resp


class ThriftServer(threading.Thread):
    def run(self):
        handler = WxHelperHandler()
        processor = WeiXinHelperService.Processor(handler)
        transport = TSocket.TServerSocket(host='192.168.0.104', port=16801)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()

        server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
        # server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
        server.serve()