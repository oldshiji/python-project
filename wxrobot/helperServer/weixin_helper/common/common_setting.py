# -*- coding: utf-8 -*-



__author__ = 'jerry'

import logging
from datetime import datetime as dt
import os

DEVELOP = True

PROD_LIST = ['server-wap', 'server-quote']

f = None
try:
    f = open(os.path.expanduser('~') + '/server_name')
    if f:
        name = f.read().strip()
        if name in PROD_LIST:
            DEVELOP = False
except FileNotFoundError as e:
    pass
finally:
    if f:
        f.close()

if DEVELOP:
    APP_SERVER_IP = '127.0.0.1'
    FILE_SERVER_IP = '192.168.0.7'
    DB_SERVER_IP = '101.132.245.172'
    MONGO_IP = '192.168.0.7'
    Redis_IP = '101.132.245.172'
    Redis_Port = 6379
    Redis_Passwd = "wxhelper~!@"
    SQL_DB_CONNECTION_STR = 'mysql+mysqldb://root:zxroot@%s:3306' % DB_SERVER_IP
    # SQL_DB_CONNECTION_STR = 'mysql+mysqldb://udcmysql:udcmysql@2017@%s:3306' % DB_SERVER_IP

else:
    APP_SERVER_IP = '10.105.15.68'
    FILE_SERVER_IP = '115.159.54.121'
    DB_SERVER_IP = '10.105.5.187'
    MONGO_IP = '10.105.15.68'
    Redis_IP = '101.132.245.172'
    Redis_Port = 6379
    Redis_Passwd = "wxhelper~!@"
    SQL_DB_CONNECTION_STR = 'mysql+mysqldb://username:passwd@%s:3306' % DB_SERVER_IP

LOGIN_QRCODE_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'web', 'static')
hub_server_address = "tcp:2020"
wx_helper_linker_address = (APP_SERVER_IP, 2020)
ADMIN_SESSION_TAG = "wx_helper_session"
web_access_linker_address = (APP_SERVER_IP, 2020)
session_dict = {}
qr_code_map = {}
helper_dict = {}  # 格式: {uin: WxHelper()}

