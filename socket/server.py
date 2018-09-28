

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("127.0.0.1",1234))

server.listen(1)

while True:

    conn,addr = server.accept()

    recv = conn.recv(8090)
    conn.sendall(recv)
    conn.close()