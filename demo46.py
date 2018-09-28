import redis

"""
print(dir(redis))

print(r.keys("*"))

print(r.get('name'))
"""

r = redis.StrictRedis(host='127.0.0.1',port=6379,charset='utf8',decode_responses=True)

while True:

    #print(r.brpop('task',0))

    cmd = r.brpop('task',0)

    print(cmd[1])
    if cmd[1]=='a':
        print('你的消息是a')
    elif cmd[1]=='b':
        print('你的消息是b')
    elif cmd[1] =='c':
        print('你的消息是c')
    else:
        print('等待任务中...')