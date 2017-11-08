#coding=utf-8
import struct
from socket import *

#构造下载请求数据
# struct.pack http://blog.csdn.net/w83761456/article/details/21171085
#H8sb5sb 表示 pack(fmt, v1, v2, ...)    按照给定的格式(fmt)，把数据封装成字符串(实际上是类似于c结构体的字节流) 
#!H 替换1 , 8s表示文件名test.jpg 8字节 b替换0 5s 表示octet b替换0  


udpSocket = socket(AF_INET,SOCK_DGRAM);
#组包
cmd_buf = struct.pack("!H8sb5sb",1,"test.png",0,"octet",0);
#tftp 协议 规定69端口
udpSocket.sendto(cmd_buf,("192.168.1.2",69));

#解析数据
result = struct.unpack("!HH",cmd_buf[:4])
print(result);


udpSocket.close();



