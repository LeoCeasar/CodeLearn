#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Hello', b'World']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
 
