#coding=utf-8
#进程间通信 -Queue
from multiprocessing import Queue,Process
import time
#利用Queue模块实现多进程间的数据传递，Queue本身是一个消息队列程序
#先进先出
#初始化定义队列长度，超过会溢出，初始化长度可不传
#queue = Queue(3);
#put 可put进任意对象
#queue.put("haha1");

def write(q):
	for value in ["a","b","c"]:
		print ("put %s to queue "%value);
		q.put(value);
		time.sleep(1);


def read(q):
	while not q.empty():
		value = q.get();
		print ("get value --- %s from queue "%value);
		time.sleep(1);

if __name__ == "__main__":
	q = Queue();
	pw = Process(target=write,args=(q,));
	pr = Process(target=read,args=(q,));
	#启动子进程pw 开始写入
	pw.start();
	#阻塞进程，等待pw完成
	pw.join();
	

	
	pr.start();
	pr.join();
	
	print("通信完成");	



