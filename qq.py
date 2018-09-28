import requests
import demo49 as getip
import threading


url = "http://d1.web2.qq.com/channel/poll2"

header = {
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':'331',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'pgv_pvi=8819077120; RK=20rUqiuFd8; pgv_pvid=3769205834; pgv_si=s9769480192; ptisp=ctc; ptcz=4d3307193b4ed1ef84620ec31810432055ce1732eac3e39c37874ee779bf6105; uin=o1655664358; skey=@yjubjux7Z; pt2gguin=o1655664358; p_uin=o1655664358; pt4_token=4XO2AvjzN4-qvfTj-mybcmKNg5vw*bK4-6p8arvWDq0_; p_skey=waRVUmj4fk9FWccYLrqa5kc1P1EwNaQBMpUeH9oDsC0_',
'Host':'d1.web2.qq.com',
'Origin':'http://d1.web2.qq.com',
'Referer':'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

data = {
    'r':'{"ptwebqq":"","clientid":53999199,"psessionid":"8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857","key":""}',
}


param = {


}

temp = {"result":[{"poll_type":"group_message","value":{"content":[["font",{"color":"000000","name":"微软雅黑","size":10,"style":[0,0,0]}],"我专业代理 腾讯云域名空间服务器，对这个太了解了",""],"from_uin":2182666025,"group_code":2182666025,"msg_id":8479,"msg_type":4,"send_uin":3100055232,"time":1519884818,"to_uin":1655664358}}],"retcode":0,"retmsg":"ok"}

#print(temp['result'][0]['value']['content'])


def rest():
    print("时间到了")

while True:

    try:
        proxies = getip.get_random_ip()

        result = requests.post(url, headers=header, data=data)

        print("循环打印来自qq的消息记录\r\n")
        # print(result.text)
        content = result.text

        url1 = "http://www.itkucode.com:2349";

        param1 = {
            'event_name': 1,
            'to_connection_id': 2,
            'content': content
        }

        result1 = requests.get(url1, params=param1)

        print(result1.text)
    except:
        print("服务器拒绝响应了暂停５秒钟后继续")
        print("zzzz...")
        #sleep(5)

        threading.Timer(5,rest)

        continue






