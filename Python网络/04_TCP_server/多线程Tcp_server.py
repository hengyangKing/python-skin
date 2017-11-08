#coding=utf-8
from socket import *
from threading import Thread

def dealClient:(accept):
		newClient,clientInfo = accept;

		print("----子进程，接下来负责数据处理[%s]"%str(clientInfo));

		while True:
			recvData = newClient.recv(1024);
			if len(recvData) > 0:
				print ("recv[%s]:%s"%(str(clientInfo),recvData))
			else:
				print ("[%s]客户端已经关闭"%str(clientInfo));
				break();	
		newClient.close();

def main():
	
	server = socket(AF_INET,SOCK_STAREM);
	#重复使用绑定的信息
	server.sersockopt(SOL_SOCKET,SO_REUSEADDR,1);

	server.bind(("",7788));

	server.listen(5);
#try 能捕获强制结束server 的关闭
	try:
		while True:
		print("waiting new client coming.....");

 		accept = server.accept();

 		client = Process(target=dealClient,args=(accept,));

 		client.start();

 		#因为已经想子进程中copy了一份引用，并且父进程中这个套接字也没有用处了，so close()
 		accept[0].close();
		
	finally:
		server.close();
	
if __name__=="__main__":
	main();
