import socket
import threading
from multiprocessing import Pool,Process,Queue
import os,time,sys


class Client():
    def run(self):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(("127.0.0.1",8090))
        threading.Thread(target=self.write,args=(client,)).start()
        threading.Thread(target=self.waitShow,args=(client,)).start()

    def write(self,client):

        while True:
            self.showWelcome()
            username = str(input("请输入您的账号："))
            if not username:
                print("[Account-Error]:您输入的账号错误")
                return 0
            qq = str(input("请输入您的qq号："))
            if not qq:
                print("[Account-Error]:请输入您的qq号")

            message = self.send(username,qq)

            if data:
                client.send(message.encode("utf8"))

    def send(self,data1,data2):
        return "%s-%s"%(data1,data2)

    def showWelcome(self):

        print("************************************************************")
        print("**         [@username]单聊                                **")
        print("**         [@info-username] 查看用户信息                   **")
        print("**         [@sum]查看好友数量                              **")
        print("**                                                        **")
        print("**                                                        **")
        print("**                                                        **")
        print("**                                                        **")
        print("**                                                        **")
        print("************************************************************")

    def waitShow(self,client):
        while True:
            data = client.recv(1024)
            if data:
                msg = data.decode("utf8")
                source = str(msg).split(':')
                who = source[0]
                message = source[1]

                print("\r\n用户[%s]say：%s"%(who,message))

if __name__ == '__main__':
    client = Client()
    client.run()