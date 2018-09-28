import socket
import threading

from multiprocessing import Pool,Process,Queue
import os,time,sys
event = threading.Event()
local = threading.local()

class Server():
    def __init__(self):
        self.clientList = {}
        self.clientNum = 0
    def run(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind(("0.0.0.0",8090))
        server.listen(10)
        while True:
            client, ip = server.accept()
            if client:
                #每次接受数据创建一个线程
                threading.Thread(target=self.acceptClient, args=(client,)).start()

    def acceptClient(self,client):
        while True:
            if client:
                #接受当前客户端的数据
                data = client.recv(1024)
                #当前数据解码
                data = data.decode("utf8")
                self.parseRequest(client,data)

    def parseRequest(self,client,data):
        if data:
            request = data.split(":")
            #请求的模块    view.user
            serviceName = request[0]
            #动作         register
            actionName  = request[1]
            # 请求参数    name,qq
            params = request[1:]
            obj = __import__('view.'+serviceName,fromlist=True)
            o = controller()
            if hasattr(o,serviceName):
                action = getattr(o,actionName)
                action()
            else:
                print("404")
            print(serviceName,actionName)
            client.send(actionName.encode("utf8"))








if __name__ == '__main__':
    Server = Server()
    Server.run()