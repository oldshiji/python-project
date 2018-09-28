import redis


def getone()->'返回redis的一个字符类型数据':
    r = redis.StrictRedis(host='localhost',port='6379',encoding='utf8',decode_responses=True,db=0)

    if r.exists("name"):
        return r.get("name")
    else:
        return None