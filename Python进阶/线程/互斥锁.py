#coding=utf-8
#互斥锁 条件不满足阻塞等待 条件满足执行
#保证多个线程对同一个资源产生资源竞争时， 
#创建锁
#mutex = threading.Lock();
#锁定
#mutex.acquire([blocking]);
#释放
#mutex.release();
#其中，锁定方法acquire可以有一个blocking参数，True为当前线程会阻塞，直接获取到这个锁为止，False当前线程不会阻塞

import time
from threading import Thread,Lock

num = 1;
#创建互斥锁	
mutex = Lock();

#work1 和 work2 两个线程都抢着执行，对两个work都上锁，如果有一方成功上锁，会导致另外一方会阻塞直到锁被解开为止
def work1():
	global num
	global mutex;
	#添加互斥锁
	mutex.acquire();
	for i in range(1000000):
		num+=1;
	print("work1"+str(num));
	mutex.release();

def work2():
	global mutex;
	#添加互斥锁
	mutex.acquire();
	global num
	for i in range(1000000):
		num+=1;
	print("work2"+str(num));	
	mutex.release();

def test():
	t1 = Thread(target=work1);
	t1.start();
	
	#time.sleep(1);
	t2 = Thread(target=work2);
	t2.start();

if __name__=="__main__":
	for i in range(10):
		test();

	print(num);

