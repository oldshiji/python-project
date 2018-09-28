import socket
import threading

from multiprocessing import Pool,Process,Queue
import os,time,sys
import view.user

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

        #在开启一个线程通知客户端用户的情况
        #threading.Thread(target=self.userInfo,args=(server,)).start()
        while True:
            client, ip = server.accept()
            if client:
                #每次接受数据创建一个线程
                threading.Thread(target=self.saveClient, args=(client,)).start()

    def cmd(self,cmd,client):
        print(cmd)
        if cmd=='people':
            people = '['
            for item in self.clientList.values():
                if type(item) is str:
                    people+=item+','

            people = people[0:-1]
            people+=']'
            client.send(people.encode("utf8"))
        elif cmd=='help':
            messsage = '''
            *******************************************************************************
            **  [people]返回当前用户列表　　[help]返回可用命令列表                       
            **                                                                            
            **  [username@msg]单独给某人发消息                                             
            **                                                                           
            *******************************************************************************
            '''
            client.send(messsage.encode("utf8"))

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
            if '+' in data:
                cmd = data[1:]
                self.cmd(cmd,client)

            if '-' in data:
                #账号注册请求处理
                register = data.split("-")
                username = register[0]
                qq       = register[1]
                user = view.user.User(username,qq,client)
                ret = user.register()

                if ret['status']==0:
                    message = str("fail") + "-" + ret['info']
                    client.send(message.encode("utf8"))
                elif ret['status']==1:


                    # 用户聊天请求处理
                    # 保存客户端对象映射字典
                    self.clientList[username] = client
                    self.clientList[client] = username


                    message = str("ok") + "-" + username
                    client.send(message.encode("utf8"))

            if '@' in data:
                #一对一聊天

                source = data.split('@')
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



            if ':' in data:
                source = data.split(':')
                # 指定发送的用户名
                who = source[0]
                # 发送的消息内容
                msg = source[1]

                client1 = self.clientList[who]
                from_who = self.clientList[client]

                # 格式：用户：信息
                message = str(from_who) + ":" + str(msg)
                for client in self.clientList.keys():
                    if type(client) is str:
                        pass
                    else:

                        client.send(message.encode("utf8"))




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