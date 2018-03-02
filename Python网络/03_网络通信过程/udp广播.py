#coding=utf-8

import sys
from socket import *
#单播 点对点
#多播 一对多
#广播 一对所有

#192.168.x.0 --- 网络号
#192.168.x.255 --- 广播地址

socket = socket.socket(AF_INET,SOCK_DGRAM);
socket.setsockopt(SOL_SOCKET,SO_BROADCAST,1);

#发送到广播地址7788端口 <broadcast> 为更通用写法
socket.sendto("Hi",("<broadcast>",7788));




