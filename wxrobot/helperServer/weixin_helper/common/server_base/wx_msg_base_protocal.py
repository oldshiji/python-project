# -*- coding: utf-8 -*-
from twisted.internet import protocol
from twisted.internet import threads, reactor
from twisted.python import log

from common.thrift.define.ttypes import DirectionType
from common.thrift.head.ttypes import WxHead
from common.thrift_message.message import parse_message_by_byte, WxMessage

__author__ = 'jerry'


class WxMsgBaseProtocal(protocol.Protocol):
    """
    代表一个客户端连接
    """
    _buffer = b''
    _busyReceiving = False
    _offset = 0
    msg_mapping = {}

    def dataReceived(self, data):
        if self._busyReceiving:
            self._buffer += data
            return

        try:
            self._busyReceiving = True
            self._buffer += data
            while True:
                msg, total_len = parse_message_by_byte(self._buffer, 0)
                if msg:
                    try:
                        self.__msg_resolve(msg)
                    except BufferError:
                        log.err()
                    self._offset = total_len + 4
                    self._buffer = self._buffer[self._offset:]
                    self._offset = 0
                else:
                    break
        except BufferError:
            log.err()
            # logger.error(traceback.format_exc())
            self._buffer = b''
            self._offset = 0
        finally:
            self._busyReceiving = False

    def __msg_resolve(self, msg):
        """
        消息体解析，以及分配处理函数
        :param msg:
        :return:
        """
        flag = False
        for (func, item) in self.msg_mapping.items():
            if msg.head.appId == item[0] and msg.head.functionId == item[1]:
                flag = True
                body = item[2]()
                # TODO 消息体解析逻辑
                # body.ParseFromString(msg.bodyBuf)
                msg.parse_body_by_byte(body)

                if hasattr(self, func.__name__):
                    is_asyn = item[3]
                    if not is_asyn:
                        func(self, msg)
                    else:
                        d = threads.deferToThread(eval('self.%s' % func.__name__), msg)
                        d.addErrback(self.error_callback, msg)

        if not flag:
            self.unresolve_msg(msg)

    def unresolve_msg(self, msg):
        pass

    def error_callback(self, e, msg):
        log.err(e)

    def send_msg_to_hub(self, app_id=None, function_id=None, body=None, server_token_id=None):
        head = WxHead()
        head.appId = app_id
        head.functionId = function_id
        head.direction = DirectionType.ToHubServer
        if server_token_id:
            head.serverTokenId = server_token_id
        self.transport.write(WxMessage(head=head, body=body).to_bytes_with_body())

    def send_msg(self, msg=None, head=None, body=None, use_raw_buf=False, call_from_thread=False):

        def _send_msg(_msg=None, _head=None, _body=None, _use_raw_buf=False):
            if _msg:
                if _use_raw_buf:
                    self.transport.write(_msg.to_bytes_with_raw_data())
                else:
                    self.transport.write(_msg.to_bytes_with_body())
            else:
                self.transport.write(WxMessage(head=_head, body=_body).to_bytes_with_body())

        if call_from_thread:
            reactor.callFromThread(_send_msg, msg, head, body, use_raw_buf)
        else:
            _send_msg(msg, head, body, use_raw_buf)
