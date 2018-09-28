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

""""
data = {
        'imgUrl':imgurl,
        #'scenes':[
            #'ocr',#:通用文字识别
            #'politician',#：政治敏感识别
            #'antiporn',#：色情识别
            #'terror',#：暴恐识别
            #'webimage',#：网络图片文字识别
            #'disgust',#: 恶心图像识别
            #'watermark',#: 广告检测
            #'quality',#: 图像质量检测
            #'accurate',#：通用文字识别（高精度含位置版）
            #'accuratebasic',#：通用文字识别（高精度版）
        #]
    }
     #headers = {'Content-Type':'application/json;charset=utf-8'}
"""

def imgsencer()->'图像审核':

    imgurl = "http://t1.mmonly.cc/uploads/tu/201604/83/4lnp1tin45v.jpg"
    #imgurl = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1517988565930&di=47ce9094fd8cbc89c2f36011255a4da2&imgtype=0&src=http%3A%2F%2Fv.hinews.cn%2Fimg%2Fzhuaqu%2F20150403%2F5854150403083019.jpg"
    #imgurl = "http://img1.qq.com/tech/pics/8081/8081022.jpg"
    #url = config.img_censor
    url = config.user_defined

    access_token = getAccessToken()
    params = {'access_token':access_token}

    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    #headers = {'Content-Type': 'application/json;charset=utf-8'}

    data = {'imgUrl':imgurl}


    r = requests.post(url,params=params,headers=headers,data=data)

    print(r.json())



imgsencer()




