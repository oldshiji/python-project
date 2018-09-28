# -*- coding: utf-8 -*-

import json
import struct
from twisted.python import log
from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TTransport import TMemoryBuffer


def serialize_object(obj):
    """
    序列化 thrift 对象
    :param obj:
    :return:
    """
    memory = TMemoryBuffer()
    binary_protocol = TBinaryProtocol(memory)
    obj.write(binary_protocol)
    return memory.getvalue()
