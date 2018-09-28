import urllib.request

import json
import ssl
import urllib.parse


url = "http://118.24.77.117:9501/admin/Index/memory"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
req = urllib.request.Request(url,headers=headers)
context = ssl._create_unverified_context()

response = urllib.request.urlopen(req,context=context)

print(response.read().decode("utf8"))


