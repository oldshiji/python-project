import redis

r = redis.StrictRedis(host='localhost',port=6379)

./configure --with-php-config=/home/soft/php/bin/php-config --enable-async-redis