import requests
import json

"""
url = "http://www.baidu.com"
f = open("baidu1.html",mode='w',encoding='utf8')

f.write(response.text)

f.close()
response = requests.get(url,params=param)
response = requests.post(url)
response = requests.put(url)
response = requests.delete(url)
response = requests.head(url)
response = requests.options(url)
print(response.url)


print(response.text)
print(response.content)
response = requests.post(url)

#print(response.text)
#print(response.json())

#print(response.json(response.text))

print(response.raise_for_status())
print(response.status_code)
print(response.text)
print(response.json())
print(response.content)
print(response.encoding)
r = requests.get(url,stream=True)

print(r.text)
print(r.content)
print(r.encoding)
print(r.raise_for_status())
print(r.status_code)
print(r.raw)
print(r.raw.read(100))
url = "http://www.app.com/app/date1.php"
param = {'name':'张三','age':'100','address':'上海'}
header = {'user-agent':'pyapp'}
r = requests.post(url,headers=header)
print(r)
dir(r)
datas = {'name':'tony','age':'200','address':'america'}
datas = (('key1','value1'),('key2','value2'))
#json format data
datas = {'name':'tony','age':100}

r = requests.post(url,data=json.dumps(datas))


#json format data
datas = {'name':'tony','age':100}


r = requests.post(url,json=datas)

print(json.dumps(datas))
print(r.text)
file = {"file":open("r1.html","rb")}
print(r.status_code==requests.codes.ok)
print(r.text)
print(r.raise_for_status())
print(r.headers)
print(r.text)
print(r.content)
print(r.raw)
#print(r.json())
print(r.url)
print(r.encoding)
print(r.request)
print(type(r.headers))
result = sorted(r.headers)
#print(r.headers)
print(result)

for w in result:
    print(w,'=',r.headers[w])
"""
url = "http://www.app.com/app/date1.php"

file = {"file":('demoa.txt','there are some data will send to the server')}

r = requests.post(url,files=file)

print(r.text)

print(r.status_code)

print(r.cookies)

print(r.history)