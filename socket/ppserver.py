from multiprocessing import Pool

import os,time,random
import socket


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",9090))

server.listen(10)

def runp(client,address):
    print("服务器子进程启动-----%d"%(os.getpid()))
    while True:
        data = client.recv(1024)
        if data:
            print("来自客户端的数据是：%s" % (data.decode("utf8")))
            client.send(data)
        else:
            print("暂时还没有人连接服务器")


if __name__=='__main__':
    print("服务主进程启动----------")
    #有客户端进来创建一个子进程处理
    client, address = server.accept()

    pclient = Pool(2)
    if client:
        pclient.apply_async(runp,args=(client,address))

    pclient.close()
    pclient.join()

    print("服务主进程结束----------")



