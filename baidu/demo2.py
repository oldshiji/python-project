import requests
import config
import redis
import json
import urllib

#缓存数据
def cache(data,type,time=0)->'data：缓存的数据,type:缓存的方式,time:缓存的时间':
    r = redis.StrictRedis(host='localhost',port='6379',db=1,charset='utf8')
    if type=='set':
        r.set(data['key'],data['value']) #字符串缓存　key=value
        if time>0:
            r.expire(data['key'],time)  #字符串缓存周期　　单位时间是秒
    elif type=='get':
        result = r.get(data['key'])


    return result

#获取access_token并缓存
def getAccessToken():
    params = {
        'grant_type':'client_credentials',
        'client_id':config.api_key,
        'client_secret':config.secret_key
    }

    url = config.accesstoken_url
    #先读取缓存是否存在
    access_token = cache({'key':'access_token'},type='get')
    if access_token:
        return access_token
    else:
        r = requests.post(url, params=params)
        json = r.json()
        access_token = json['access_token']
        expires_in = json['expires_in']
        cache({
            'key':'access_token',
            'value':access_token
        },type='set',time=expires_in)
        return access_token



access_token = getAccessToken()



def textInspect(accessToken,text)->'文本检测':

    url = "https://aip.baidubce.com/rest/2.0/antispam/v1/spam"

    param = {
        'access_token':accessToken
    }

    data = {
        'command_no':'500071',
        'content':text
    }

    header = {
        'Content-Type':'application/x-www-form-urlencoded'
    }


    result = requests.post(url,params=param,headers=header,data=data)

    print(result.json())





text = '如果你有什么问题，可以加我扣扣45686486'

textInspect(access_token,text)
