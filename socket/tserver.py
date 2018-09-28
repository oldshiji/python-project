import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",9502))

while True:
    data = str(input("请输入数据："))

    client.send(data.encode("utf8"))

    print(client.recv(1024))
