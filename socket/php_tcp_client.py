import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

res = client.connect(("123.56.12.53",2346))


while 1:
    data = str(input("请输入数据："))
    if data:
        client.send(data.encode("utf8"))

        print(client.recv(8190))
    else:
        print("你啥也没有输入")



