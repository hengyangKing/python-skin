#coding=utf-8
from socket import *

#1.创建socket tcp 模式为 sock_stream
serverSocket = socket(AF_INET,SOCK_STREAM);

#2.绑定端口
serverSocket.bind(("",8899));
print("-----------1")
#3.变成被动socket
serverSocket.listen(5);

print("-----------2")
#4.accept() 返回元组
#若有信的客户端链接服务器，那么就产生一个新的套接字专门为这个客户端服务器
#clientSocket 用来专门为这个客户端服务
#serverSocket 就可以省下来专门等待其他信的客户端的链接
#clientInfo 中包含这个client的ip & port 

print("-----------3")

#accept 有阻塞功能

clientSocket,clientInfo = serverSocket.accept();

print("-----------4")

#5.客户端socket 准备接受数据
recvData = clientSocket.recv(1024) 
print("%s:%s"%(str(clientInfo),recvData));


clientSocket.sendto("hahahahha",(clientInfo[0],clientInfo[1]));


clientSocket.close();
serverSocket.close();


print("-----------5")






