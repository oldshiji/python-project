import socket
import threading
from multiprocessing import Pool,Process,Queue
import os,time,sys

local = threading.local()
event = threading.Event()
class Client():
    def __init__(self,user):
        self.isLogin = False
        self.user = user
    def run(self):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(("127.0.0.1",8090))
        threading.Thread(target=self.request,args=(client,)).start()
        threading.Thread(target=self.response,args=(client,)).start()

    def request(self,client):

        while True:
            service = str(input("请输入url:"))
            if service:
                client.send(service.encode("utf8"))



    def response(self,client):

        while True:
            data = client.recv(1024)
            data = data.decode("utf8")
            print(data)

if __name__ == '__main__':
    local.user = '未登录'
    client = Client(local.user)
    client.run()