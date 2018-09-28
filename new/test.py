import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("123.56.12.53",8888))

client.send("GET /index.html HTTP/1.1")

print(client.recv(1024))