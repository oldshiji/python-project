import os
import time
import random
import hashlib
import math

config  = {
    "port":9888
}

settings = {
    "debug":False,
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template")
}



#数据库配置
dbconfig = {
    "host":"127.0.0.1",
    "port":"3306",
    "user":"root",
    "pwd":"123456",
    "dbname":"webim",
    "charset":"utf8"
}
