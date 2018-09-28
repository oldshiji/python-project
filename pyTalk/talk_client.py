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
        threading.Thread(target=self.write,args=(client,)).start()
        threading.Thread(target=self.response,args=(client,)).start()

    def write(self,client):

        while True:

            self.showWelcome()
            if not self.isLogin:
                self.register(client)


            time.sleep(2)
            self.talk(client)


    def register(self,client):

        username = self.getInput("请输入您的账号：")
        qq = self.getInput("请输入您的qq号：")
        message = self.registerDataFormatter(username, qq)
        if message:
            client.send(message.encode("utf8"))


    #获取输入的数据
    def getInput(self,msg):
        return str(input(msg))
    def talk(self,client):
        while True:
            data = self.getInput("")
            if data:
                if '@' not in data:
                    if '+' in data:
                        message = data

                        client.send(message.encode("utf8"))
                    else:
                        message = self.user + ":" + data

                        client.send(message.encode("utf8"))

                else:
                    client.send(data.encode("utf8"))


    #注册数据格式化
    def registerDataFormatter(self,data1,data2):
        return data1+"-"+data2

    def showWelcome(self):
        print("************************************************************")
        print("**                                                        **")
        print("**                  Welcome to use                        **")
        print("**                                                        **")
        print("************************************************************")

    #数据响应解析
    def responseParse(self):
        pass

    def response(self,client):

        while True:
            data = client.recv(1024)
            data = data.decode("utf8")
            if data:
                if '-' in data:
                    #用户注册响应
                    source = str(data).split('-')
                    message = source[1]
                    status = source[0]
                    if status=='ok':
                        self.isLogin = True
                        self.user = message
                        print("\r\n注册成功！您的账号是：%s\r\n" % (message))
                        print("*******************系统正在进入聊天系统**********************")

                    elif status=='fail':
                        print("\r\n%s"%(message))



                elif ':' in data:
                    source = str(data).split(':')
                    message = source[1]
                    from_who = source[0]

                    print("用户[%s]say：%s" % (from_who,message))

                else:
                    #命令响应
                    print("%s" % (data))

if __name__ == '__main__':
    local.user = '未登录'
    client = Client(local.user)
    client.run()