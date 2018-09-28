import socket
import threading
from multiprocessing import Pool,Process,Queue
import os,time,sys

event = threading.Event()
local = threading.local()

class Server():
    def __init__(self):
        self.clientList = {}
    def run(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind(("0.0.0.0",8090))
        server.listen(10)

        while True:
            client, ip = server.accept()
            if client:
                #每次接受数据创建一个线程
                threading.Thread(target=self.saveClient, args=(client,)).start()


        #threading.Thread(target=self.read).start()

    def saveClient(self,client):
        while True:
            if client:
                #接受当前客户端的数据
                data = client.recv(1024)
                #当前数据解码
                data = data.decode("utf8")
                self.parseData(client,data)

    def parseData(self,client,data):
        if data:
            if '-' in data:
                #账号注册请求处理
                register = data.split("-")
                username = register[0]
                qq       = register[1]


            if ':' in data:
                #用户聊天请求处理
                # 保存客户端对象映射字典
                self.clientList[data] = client
                self.clientList[client] = data
            else:
                source = data.split(':')
                # 指定发送的用户名
                who = source[0]
                # 发送的消息内容
                msg = source[1]

                # 得到发送者对象
                client1 = self.clientList[who]
                from_who = self.clientList[client]

                # 格式：用户：信息
                message = str(from_who) + ":" + str(msg)
                client1.send(message.encode("utf8"))



    def waitShow(self,client,ip):
        pass

    def read(self):
        while True:
            clientAll = self.clientList
            for client in clientAll.keys():
                event.wait()
                words = clientAll.get(client).recv(1024)

                print("客户端%s说:%s" % (client, words.decode("utf8")))
                clientAll.get(client).send(words)
                event.clear()





if __name__ == '__main__':
    Server = Server()
    Server.run()