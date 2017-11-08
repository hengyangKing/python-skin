#coding=utf-8
from multiprocessing import Pool
import time
import os

def test():
#	print(os.getpid());
#	print(os,getppid());
	print("----进程池中的进程----pid==%s and ppid=%s"%(os.getpid(),os.getppid()));
	for i in range(3):
		print("------%d------"%i);
		time.sleep(1);
	#return "foo";



def test2(args):
	print("----callback func---pid=%d"%os.getpid());
	print("----callback func---args=%s"%args);

pool = Pool(3);
pool.apply_async(func=test,callback=test2);
pool.close();
pool.join();
time.sleep(5);
print("----主进程---pid=%d"%os.getpid());

print("callback 作用于异步回调函数func ，完成的调用，其回调线程在主线程,其中异步线程函数返回值将作为回调函数的参数")



