import requests

url ="http://www.app.com/app/card.php"

#r = requests.get(url)
#r = requests.post(url)
#r = requests.delete(url)
#r = requests.put(url)
#r = requests.head(url)
#r = requests.patch(url)
""""
querystring = {'name':'tony','age':100}
r = requests.get(url,params=querystring)
print(r.url)
print(r.text)

for x in r.json():
    print(x)
    print(r.json())
print(r.raise_for_status())
print(r.status_code)
r = requests.post(url)
r = requests.post(url,stream=True)

print(r.text)
print(r.raw)
print(r.raw.read(100))

headers = {'user-agent':'jackcsm'}

r = requests.post(url,headers=headers)

print(r.text)
print(r.content)
r = requests.post(url,data={'name':'tony','age':100})

print(r.text)
print(r.content)
files = {'file':open("new/text.txt","rb")}

r = requests.post(url,files=files)

print(r.text)
print(r.content)
"""

files = {'file':('xxx.txt','there are many trees will be cut')}

r = requests.post(url,files=files)

print(r.text)
print(r.headers)


