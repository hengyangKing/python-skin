#coding=utf-8

from socket import *

serverSocket = socket(AF_INET,SOCK_STREAM);

serverSocket.bind(("",7878));

servetSocket.listen(5);

while True:

	newClient,clientInfo = serverSocket.accept();

	while True:
		recvData = newClient.recv(1024);
		#若接受的长度为0 则意味着客户端关闭了链接
		if len(recvData) == 0:
			print("%s"%recvData);
		else:
			break;
		
		newClient.send("get new massage");

	newClient.close();

serverSocket.close();
 
