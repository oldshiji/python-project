import sys
import time
import hashlib
import requests
from lxml import etree

import json
def proxy(url):
    #requests.packages.urllib3.disable_warnings()
    _version = sys.version_info

    is_python3 = (_version[0] == 3)

    # 个人中心获取orderno与secret
    #orderno = "DT20180710184042Iy3FOYMz"
    orderno = "GB20180711155300jM37arJU"
    secret = "3d3246ea2ee284b57cdec9671886393f"

    #ip = "dynamic.xiongmaodaili.com"
    ip = "114.246.98.217"
    #port = "8088"
    port = "36330"

    ip_port = ip + ":" + port

    timestamp = str(int(time.time()))  # 计算时间戳
    txt = ""
    txt = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

    if is_python3:
        txt = txt.encode()

    md5_string = hashlib.md5(txt).hexdigest()  # 计算sign
    sign = md5_string.upper()  # 转换成大写
    # print(sign)
    auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

    # print(auth)
    proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
    headers = {"Proxy-Authorization": auth}

    '''
     #r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    #r = requests.get(url, headers=headers, proxies=proxy)
    #print(r.status_code)
    #print(r.content)
    #print(r.status_code)
    if r.status_code == 302 or r.status_code == 301:
        loc = r.headers['Location']
        url_f = url + loc
        #print(loc)
        r = requests.get(url_f, headers=headers, proxies=proxy)
        #print(r.status_code)
        #print(r.text)

    return r.text
 return {
        "proxy":proxy,
        "headers":headers
    }
    '''
    r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    if r.status_code == 302 or r.status_code == 301:
        loc = r.headers['Location']
        url_f = url + loc
        r = requests.get(url_f, headers=headers, proxies=proxy)
    print(r.text)

if __name__=='__main__':
    url = "https://www.zhipin.com/c101190400-p100109/h_101190400/?page=8&ka=page-8"
    proxy(url)

    '''
    r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    if r.status_code == 302 or r.status_code == 301:
        loc = r.headers['Location']
        url_f = url + loc
        r = requests.get(url_f, headers=headers, proxies=proxy)

    return r.text
    '''



