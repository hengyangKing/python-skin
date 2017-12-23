#coding=utf-8
#epoll 相较于  select 版本 没有数量上限 更不采用轮询机制来完成检测 
#而使用更高级的事件通知机制
# 
import select
from socket import *
def main():
		socket = socket.socket(AF_INET,SOCK_STREAM);
		socket.setsockopt(SOL_SOCKET,SO_REUSEADDR);

		socket.bind(("",7788));

		s.listen(1);

		#创建一个epoll对象
		epoll = select.epoll();

		#注册事件
		#socket.fileno() 返回套接字所对应的文件描述符 简称fd
		#epoll.register(fd[,eventmask])
		#其中 fd已经注册过，则会发生异常
		#将创造的socket 添加到epoll 的事件监听中
		#检测类型 select.EPOLLIN socket 可读 
		#select.EPOLLET socket ET模式 当epoll 检测到目和描述事件发生并将词事件通知应用程序
		#应用程序必须立刻处理该事件
		#select.EPOLLOUT socket 可写
	
		epoll.register(socket.fileno(),select.EPOLLIN|select.EPOLLET);

		connections = {};
		addresses = {};

		#等待客户端的到来
		while True:
			#epoll 进行 fd 扫描的地方 未指定超时时间则为阻塞等待
			#得到epoll_list 为 poll()中 哪些可以收发写
			#
			epoll_list = epoll.poll();
			#fd 文件描述符 event 为该socket 的具体当前可操作类型
			#
			for fd,events in epoll_list:

				if fd = socket.fileno():
					#若是socket 创建的套接字被激活
					conn,addr = socket.accept();

					print ("new client join")

					connections[conn.fileno()] = conn;
					addresses[conn.fileno()] = addr;

					#向epoll 中注册连接的socket client 的可读事件
					epoll.register(conn.fileno(),select.EPOLLIN|select.EPOLLET)

				elif events == select.EPOLLIN:
						#从fd上接收
						recvData = connections[fd].recv(1024);
						if len(recvData)>0:
							print("recv:%s"%recvData);
						else:
							#从epoll中移除该socket client 的fd 
							epoll.unregister(fd);
							#close client socket
							connections[fd].close();

