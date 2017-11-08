#coding=utf-8
from socket import *

if __name__ == "__main__":
	print("i'm get massage and i'm port is 7777");

	udpSocket = socket(AF_INET, SOCK_DGRAM);
	udpSocket.bind(("",7777));
	num = 1;
	while True:
		recvInfo = udpSocket.recvfrom(1024);
		print(recvInfo);
		udpSocket.sendto(recvInfo[0],recvInfo[1]);
		num+=1;
		print("已经手动的第%d个数据返回给对方，内容为%s"%(num,recvInfo[0]))
		
	udpSocket.close();
