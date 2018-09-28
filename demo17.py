import requests
import json
import time
import redis
import pymysql

#url = 'http://www.sojson.com/api/qqmusic/8446666'
url = 'http://www.sojson.com/open/api/weather/json.shtml'
param = {'city':'苏州'}
r = requests.get(url,params=param)

print(r.status_code)


response = r.text
resj = r.json()

if 'data' in response:
    #print(resj['data']['shidu'])
    #print('exists')
    #print(resj)
    print('温度','PM25','PM10','质量','温度','感冒','昨天','风向')

    for w in resj['data']:
        print(resj['data'][w])