import socket
import sys

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
prot=9999
serversocket.bind((host,prot))
serversocket.listen(5)
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msga = '欢迎访问菜鸟教程！' + "\r\n"

    clientsocket.send(msga.encode('utf-8'))
    clientsocket.close()