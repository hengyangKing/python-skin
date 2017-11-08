#coding=utf-8
import os
import time
#fork() 产生一个新的子进程并返回向下执行，同时会返回当前进程，同样也向下执行，
#其中主进程ret >0 子进程ret = 0

#getpid() pid 得到该进程的id 
#getppid() ppid 得到该进程的父进程的id


ret = os.fork();
print(ret)
if ret == 0:
	while True:
		print("---1");
		print("getpid---->%s,getppid------>%s"%(os.getpid(),os.getppid()))
		time.sleep(1);
else:
	while True:
		print("---2");
		print("getpid-----%s"%os.getpid());
		time.sleep(1);



