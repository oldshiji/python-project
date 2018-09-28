import socket

while True:
    cmd = input("请输入关键字:")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(("127.0.0.1", 1234))

    client.sendall(cmd.encode())

    print(client.recv(8090))

    client.close()
