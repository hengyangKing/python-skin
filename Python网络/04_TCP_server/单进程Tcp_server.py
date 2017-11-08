#coding=utf-8
from socket import *

server = socket(AF_INET,SOCK_STAREM);
#重复使用绑定的信息
server.sersockopt(SOL_SOCKET,SO_REUSEADDR,1);

server.bind(("",7788));

server.listen(5);

print("我只能服务于一个client");
while True:
	print("waiting new client coming.....");

 	newClient,clientInfo = server.accept();

	print("----主进程，接下来负责数据处理[%s]"%str(clientInfo));
	
	try:
		while True:
			recvData = newClient.recv(1024);
			if len(recvData) > 0:
				print ("recv[%s]:%s"%(str(clientInfo),recvData))
			else:
				print ("[%s]客户端已经关闭"%str(clientInfo));
				break();

	finally:
		newClient.close();

server.close();
	
	
