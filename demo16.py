import redis

""""
r = redis.Redis(host='localhost',port='6379')

#print(r)

print(r.dbsize())

print(r.set('name','tony'))

print(r.get('name'))

r = redis.StrictRedis(host='localhost',port='6379',decode_responses=True,db=1)

print(r.set('name','tonyjack'))

print(r.get('name'))

pool = redis.ConnectionPool(host='localhost',port='6379')

r = redis.StrictRedis(connection_pool=pool,db=1,decode_responses=True)

print(r.get('name'))

"""



r = redis.StrictRedis(host='localhost',port='6379',decode_responses=True,db=1)

print(r.get('name'))
print(r.keys('*'))