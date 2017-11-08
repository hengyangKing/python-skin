#coding=utf-8
#实现单进程并发服务器
from socket import *
#创建socket

server = socket(AF_INET,SOCK_STAREM);
#重复使用绑定的信息
server.sersockopt(SOL_SOCKET,SO_REUSEADDR,1);

server.bind(("",7788));

server.listen(5);

#设置socket 为非阻塞 
#设置为非阻塞后 accept()时 若并没有客户端connect 那么accpect 会抛出一个异常
server.setblocking(False);

#保存所有保存的客户端信息
clientList = [];

while True:
 	try:
 		#等待一个新的客户端到来，既完成三次握手的客户端
 		clientSocket,clientInfo = server.accept();
 	else:
 		print("一个新的客户端到来，%s"%str(clientInfo))
 		#设置clientSocket recv也非阻塞
 		clientSocket.setblocking(False);
 		clientList.append((clientSocket,clientInfo));

 	for clientSocket,clientInfo in clientList:
 			try:
 				recvData = clientSocket.recv(1024)
 			else:
 				if len(recvData) > 0:
 					print("[%s:%s]"%(str(clientInfo),recvData));
				else:
					clientSocket.close();
					clientList.remove((clientSocket,clientInfo));
					print ("[%s]客户端已经关闭"%str(clientInfo));

server.close();
	
	


