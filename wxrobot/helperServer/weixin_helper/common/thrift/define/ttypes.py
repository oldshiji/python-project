#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class ResponseCode(object):
    Define = 0
    Succeed = 1
    Failed = 2
    ArgumentsException = 100
    NotLogin = 101
    DataException = 102
    TokenIdNotFound = 103
    TokenIdException = 104
    DataExist = 105
    LoginException = 106

    _VALUES_TO_NAMES = {
        0: "Define",
        1: "Succeed",
        2: "Failed",
        100: "ArgumentsException",
        101: "NotLogin",
        102: "DataException",
        103: "TokenIdNotFound",
        104: "TokenIdException",
        105: "DataExist",
        106: "LoginException",
    }

    _NAMES_TO_VALUES = {
        "Define": 0,
        "Succeed": 1,
        "Failed": 2,
        "ArgumentsException": 100,
        "NotLogin": 101,
        "DataException": 102,
        "TokenIdNotFound": 103,
        "TokenIdException": 104,
        "DataExist": 105,
        "LoginException": 106,
    }


class UserStatus(object):
    UserStatusDefault = 0
    Deleted = 1
    Online = 2
    Offline = 3
    Login = 4
    Logout = 5

    _VALUES_TO_NAMES = {
        0: "UserStatusDefault",
        1: "Deleted",
        2: "Online",
        3: "Offline",
        4: "Login",
        5: "Logout",
    }

    _NAMES_TO_VALUES = {
        "UserStatusDefault": 0,
        "Deleted": 1,
        "Online": 2,
        "Offline": 3,
        "Login": 4,
        "Logout": 5,
    }


class DirectionType(object):
    ToHubServer = 1
    ToWxServer = 2
    ToWebServer = 3

    _VALUES_TO_NAMES = {
        1: "ToHubServer",
        2: "ToWxServer",
        3: "ToWebServer",
    }

    _NAMES_TO_VALUES = {
        "ToHubServer": 1,
        "ToWxServer": 2,
        "ToWebServer": 3,
    }


class AppId(object):
    AppType_ServerSystem = 1
    AppType_ClientSystem = 2
    AppType_HelperServer = 3
    AppType_WebServer = 4

    _VALUES_TO_NAMES = {
        1: "AppType_ServerSystem",
        2: "AppType_ClientSystem",
        3: "AppType_HelperServer",
        4: "AppType_WebServer",
    }

    _NAMES_TO_VALUES = {
        "AppType_ServerSystem": 1,
        "AppType_ClientSystem": 2,
        "AppType_HelperServer": 3,
        "AppType_WebServer": 4,
    }


class FunctionId(object):
    ServerSystemServiceRegister = 1001
    ServerSystemHeartbeat = 1002
    ServerSystemUserStatusChange = 1003
    ClientSystemHeartbeat = 2001
    ClientSystemUpdateSession = 2002
    ClientSystemResetSession = 2003
    HelperServer_HelperLogin = 10001
    HelperServer_SendMessageToWX = 10002
    HelperServer_ReceiveMessage = 10003
    HelperServer_LoginSuccess = 10004
    HelperServer_AddFriendQR = 10005
    HelperServer_OpenGroup = 10006
    WebServer_MsgSend = 20001
    WebServer_CustomerList = 20002

    _VALUES_TO_NAMES = {
        1001: "ServerSystemServiceRegister",
        1002: "ServerSystemHeartbeat",
        1003: "ServerSystemUserStatusChange",
        2001: "ClientSystemHeartbeat",
        2002: "ClientSystemUpdateSession",
        2003: "ClientSystemResetSession",
        10001: "HelperServer_HelperLogin",
        10002: "HelperServer_SendMessageToWX",
        10003: "HelperServer_ReceiveMessage",
        10004: "HelperServer_LoginSuccess",
        10005: "HelperServer_AddFriendQR",
        10006: "HelperServer_OpenGroup",
        20001: "WebServer_MsgSend",
        20002: "WebServer_CustomerList",
    }

    _NAMES_TO_VALUES = {
        "ServerSystemServiceRegister": 1001,
        "ServerSystemHeartbeat": 1002,
        "ServerSystemUserStatusChange": 1003,
        "ClientSystemHeartbeat": 2001,
        "ClientSystemUpdateSession": 2002,
        "ClientSystemResetSession": 2003,
        "HelperServer_HelperLogin": 10001,
        "HelperServer_SendMessageToWX": 10002,
        "HelperServer_ReceiveMessage": 10003,
        "HelperServer_LoginSuccess": 10004,
        "HelperServer_AddFriendQR": 10005,
        "HelperServer_OpenGroup": 10006,
        "WebServer_MsgSend": 20001,
        "WebServer_CustomerList": 20002,
    }


class MsgType(object):
    MsgType_Text = 1
    MsgType_Hyperlink = 2

    _VALUES_TO_NAMES = {
        1: "MsgType_Text",
        2: "MsgType_Hyperlink",
    }

    _NAMES_TO_VALUES = {
        "MsgType_Text": 1,
        "MsgType_Hyperlink": 2,
    }