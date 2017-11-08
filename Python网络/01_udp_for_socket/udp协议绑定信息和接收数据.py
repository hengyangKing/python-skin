#coding=utf-8
from socket import *
#创建sorket
udpSocket = socket(AF_INET,SOCK_DGRAM);

#绑定本地的相关信息，绑定端口，如果一个网络程序不绑定，系统则会随机分配
udpSocket.bind(("",7788));#绑定ip地址和端口号，ip一般不用填写，表示本机的任何一个ip，端口号则指向了该进程

#等待接受对方发送的数据
recvData = udpSocket.recvfrom(1024);#1024表示本次接受的最大字节数

print(recvData);
#关闭
udpSocket.close();
