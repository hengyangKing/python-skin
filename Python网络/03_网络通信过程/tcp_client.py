#coding=utf-8
from socket import *

#tcp client

tcpSocket = socket(AF_INET,SOCK_STREAM);

#链接服务器

#tcp client 通过connect链接服务器后，不需要在后来的send时再次发送ip和port 
#而udp 在发送数据的时候，因为没有connect这个过程，所以需要每次都发送ip 和 port


addr = ("192.168.1.2",8899);
tcpSocket.connect(addr);

tcpSocket.send("wa hahahahhahahah");

recvData = tcpSocket.recv(1024);

print("%s"%recvData);

tcpSocket.close();


