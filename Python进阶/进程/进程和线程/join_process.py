#coding=utf-8
from multiprocessing import Process
import time
import random 


def test():
	for i in range(5):
		print ("----%d----"%i)
		time.sleep(1);

process = Process(target=test);
process.start();
#join 函数在进程中相当于一个断点，等到这个进程对象target执行完毕后，才向下执行
#相当于线程阻塞
process.join();

print("main");
