import os
import sys
import redis

""""


#cache('py','python')
print(cache('py'))
def cache(key,value='',time=0)->'redis str字符类型存储与读取':
    r = redis.StrictRedis(host='127.0.0.1',port=6379,charset='utf8',decode_responses=True)
    if key and value:
        if time!=0:
            r.set(key,value)
            r.expire(key,time)
            return True
        else:
            r.set(key,value)
            return True
    elif key:
        return r.get(key)
    else:
        print('key参数错误')

loginUid = {
    'jack':'jack@localhost#:',
    'tom':'tom@localhost#:',
    'tony':'tony@localhost#:',

}

userList = {
    'jack':['tom','tony'],
    'tom':['jack','tony'],
    'tony':['tom','jack']
}

while True:
    name = input("Your username:")
    if name in loginUid:
        while 1:
            words = input(loginUid[name])
            cache('msg', name + '说:' + words)
            print(cache('msg'))

    else:
        print("Login error")
        for x in ['chinese','japanese','america']:
    print(x)
else:
    print('over')
    
for x in [1,2,3,4,5]:
    print(x+1)
    
for x in 'chinese':
    print(x)
    pond = 3

for x in [1,2,3,4,5]:
    a = pond*x
    print(a)
    for (a,b) in [(1,2),(3,4),(5,6)]:
    print(a,b)
    for x in D:
    print(x,D[x])
    D = {'a':1,'b':2,'c':3}


for (k,v) in D.items():
    print(k,'=',v)
"""

for x in [(1,2),(3,4),(5,6)]:
    a,b = x
    print(a,b)
