import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",9090))

while True:
    data = str(input("请输入数据："))
    client.send(data.encode("utf8"))

    recv_data = client.recv(1024)

    if recv_data:
        print("来自服务器的数据：%s"%(recv_data.decode("utf8")))

