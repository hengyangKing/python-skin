#coding=utf-8


from socket import *
from threading import Thread


def getMassage():
	while True:
		info = udpSocket.recvfrom(1024);
		print(">>%s:%s"%(str(info[1]),info[0]));


def sendMassage():
	while True:
		sendInfo = input("<<:\n");
		udpSocket.sendto(sendInfo.encode("utf-8"),(destIp,destPort));

udpSocket = None;
destIp = "";
destPort = 0;
def main():	
	#修改全局变量需用global修饰
	global udpSocket,destIp,destPort;

	destIp = str(input("对方的ip:\n"));
	destPort = int(input("对方的Port:\n"));

	
	udpSocket = socket(AF_INET,SOCK_DGRAM);
	udpSocket.bind(("",6666));
	
	tr = Thread(target=getMassage);	
	ts = Thread(target=sendMassage);
	
	tr.start();
	ts.start();

	tr.join();
	ts.join();



if __name__=="__main__":
	main();
