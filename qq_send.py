import requests

url = "http://d1.web2.qq.com/channel/send_qun_msg2"

header = {
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'pgv_pvi=8819077120; RK=20rUqiuFd8; pgv_si=s6855145472; _qpsvr_localtk=0.5946439085919752; pgv_info=ssid=s1903814150; pgv_pvid=3769205834; ptisp=ctc; ptcz=4d3307193b4ed1ef84620ec31810432055ce1732eac3e39c37874ee779bf6105; uin=o1655664358; skey=@9ee5GH34N; pt2gguin=o1655664358; p_uin=o1655664358; pt4_token=rS*uNCitxPXW8G5-Ts6xdqMAjJWXOQzHQ2*rpvZeoJU_; p_skey=tD3WPQEjlHojCwDqToJscy9nKgU7bwoHaKSge3VVM-s_',
'Host':'d1.web2.qq.com',
'Origin':'http://d1.web2.qq.com',
'Referer':'http://d1.web2.qq.com/cfproxy.html?v=20151105001&callback=1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

data = {
    'r':'{"group_uin": 2636183373,"content": "[\"666\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]","face": 0, "clientid": 53999199, "msg_id": 0,"psessionid": "8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857"}',
}

result = requests.post(url, headers=header, data=data)
content = result.text
print(content)