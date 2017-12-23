
#coding=utf-8
from socket import *
# AF_INET Ipv4 协议
# SOCK_DGRAM UDP通信（数据报模式）
# SOCK_STREAM TCP通信 （流模式）

udpSocket = socket(AF_INET, SOCK_DGRAM)
#使用udp发送的数据，在每一次的是都需要写上接收方的ip和port
udpSocket.sendto("haha", ("192.168.119.210", 8080))

udpSocket.sendto("haha1", ("192.168.119.210", 8080))
