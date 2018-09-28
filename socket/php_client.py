import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("118.24.77.117",9502))

while True:
    data = str(input("please type your data:"))

    if data:
        client.send(data.encode("utf8"))

    info = client.recv(1024)

    print("receive from server:%s"%(info.decode("utf8")))