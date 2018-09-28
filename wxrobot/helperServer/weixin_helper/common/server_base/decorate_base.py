# -*- coding: utf-8 -*-

__author__ = 'jerry'

def msg_resolver(app_id, function_id, resolve_cls, is_asyn=False):
    """
    方法处理函数
    """

    def _deco(func):
        from common.server_base.wx_msg_base_protocal import WxMsgBaseProtocal
        if func not in WxMsgBaseProtocal.msg_mapping:
            WxMsgBaseProtocal.msg_mapping[func] = (app_id, function_id, resolve_cls, is_asyn)
        return func

    return _deco






