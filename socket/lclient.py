import urllib.request
import urllib.parse
import ssl
import json


url = "http://45.40.204.149:8000/semiconductor"
data = {
    "username":"jack",
    "pwd":123,
    "age":18
}
postStr = urllib.parse.urlencode(data).encode("utf8")
req = urllib.request.Request(url,data=postStr)
context = ssl._create_unverified_context()
response = urllib.request.urlopen(req,context=context)

print(response.read().decode("utf8"))