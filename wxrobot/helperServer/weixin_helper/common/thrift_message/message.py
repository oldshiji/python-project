# -*- coding: utf-8 -*-
import struct
from twisted.python import log
from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TTransport import TMemoryBuffer

from common.thrift.head.ttypes import WxHead
from common.thrift.body.ttypes import *
from common.utils.thrift_utils import serialize_object

__author__ = 'jerry'


class WxMessage:
    """
    消息定义
    """

    headBuf = b''
    bodyBuf = b''
    head = None
    body = None

    def __init__(self, head=None, body=None):
        self.head = head
        self.body = body

    def to_bytes_with_body(self):
        self.headBuf = serialize_object(self.head)
        self.bodyBuf = serialize_object(self.body)
        head_len = len(self.headBuf)
        body_len = len(self.bodyBuf)
        total_len = head_len + body_len + 8
        total_bytes = struct.pack('<ii%dsi%ds' % (head_len, body_len), total_len,
                                  head_len, self.headBuf, body_len,
                                  self.bodyBuf)
        # print("head_len={}, body_len={}, total_len={}".format(head_len, body_len, total_len))
        return total_bytes

    def to_bytes_with_raw_data(self):
        self.headBuf = serialize_object(self.head)
        head_len = len(self.headBuf)
        body_len = len(self.bodyBuf)
        total_len = head_len + body_len + 8
        total_bytes = struct.pack('<ii%dsi%ds' % (head_len, body_len), total_len,
                                  head_len, self.headBuf, body_len,
                                  self.bodyBuf)
        return total_bytes

    def parse_body_by_byte(self, body_cls):
        """
        将对象内的二进制bodyBuf解析成对象body
        :return:
        """
        if self.bodyBuf:
            # 实例化 thrift 对象
            # body_obj = body_cls()
            t_memory = TMemoryBuffer(self.bodyBuf)
            t_binary_protocol = TBinaryProtocol(t_memory)
            body_cls.read(t_binary_protocol)

            self.body = body_cls


def parse_message_by_byte(byte, offset):
    """
     从原始byte数据转换到MTMessage
     :param byte: byte数组
     :param offset: 偏移量
     :return: MTMessage 或者 None
     """
    try:
        int_len = 4
        if not byte or len(byte) < int_len:
            return None, 0

        msg = WxMessage()
        total_len = struct.unpack_from('i', byte, offset)[0]
        if len(byte) < total_len + int_len:
            return None, 0

        offset += int_len
        head_len = struct.unpack_from('i', byte, offset)[0]

        offset += int_len
        msg.headBuf = struct.unpack_from('<%ds' % (head_len,), byte, offset)[0]

        head = WxHead()
        t_memory_o = TMemoryBuffer(msg.headBuf)
        t_binary_protocol_o = TBinaryProtocol(t_memory_o)
        head.read(t_binary_protocol_o)

        if head:
            msg.head = head

        offset += head_len
        body_len = struct.unpack_from('i', byte, offset)[0]

        offset += int_len
        msg.bodyBuf = struct.unpack_from('<%ds' % (body_len,), byte, offset)[0]

        return msg, total_len

    except BufferError as e:
        log.err()
        return None, 0

