import socket


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",9090))
server.listen(10)

client,address = server.accept()

while True:
    data = client.recv(1024)
    if data:
        print("来自客户端的数据是：%s"%(data.decode("utf8")))
        client.send(data)
    else:
        print("暂时还没有人连接服务器")

