import redis


r = redis.StrictRedis(host='localhost',port='6379',db=1,charset='utf8')

#print(r.keys("*"))
""""
while True:
    result = r.brpop('message', 0)
    if result:
        print(result)
    else:
        print("wait...")
"""






