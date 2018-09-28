import urllib.request

import json
import urllib.parse
import ssl



url = "http://118.24.77.117:9501/admin/Wechat/wechat";

data = {
    "name":"jack",
    "age":100
}

def request(url,data):
    postStr = urllib.parse.urlencode(data).encode("utf8")

    req = urllib.request.Request(url, data=postStr)

    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read().decode("utf8")

ret = request(url,data)
print(ret)

