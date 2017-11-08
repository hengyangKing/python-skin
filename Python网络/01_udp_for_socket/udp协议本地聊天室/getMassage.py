#coding=utf-8
from socket import *

if __name__ == "__main__":
	print("i'm get massage and i'm port is 7777");

	udpSocket = socket(AF_INET, SOCK_DGRAM);
	udpSocket.bind(("",7777));

	while True:
		recvInfo = udpSocket.recvfrom(1024);
		# print("[%s:%s] send massage :%s"(recvInfo[1][0],str(recvInfo[1][1]),recvInfo[0].decode("utf-8")));
		print(recvInfo);
	udpSocket.close();