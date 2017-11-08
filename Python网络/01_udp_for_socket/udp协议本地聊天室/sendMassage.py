#coding=utf-8
from socket import *

def main():
	udpSocket = socket(AF_INET, SOCK_DGRAM);
	udpSocket.sendto("xxx".decode("utf-8"), ("192.168.1.2", 7777))
	
	info=udpSocket.recvfrom(1024);
	print(info);


if __name__=="__main__":
	main();
