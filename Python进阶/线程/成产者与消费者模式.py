#coding=utf-8
from threading import Thread,Lock
import time

#python 的 Queue模块中提供了同步的，线程安全的队列类 
#包括:
#FIFO（先入先出）队列Queue
#LIFO (先入后出) 队列lifoQueue
#优先级队列 priorityQueue

#上述队列都实现了锁原语（可理解为原子操作，要么不做，要么做完），能够在多线程中直接使用可以使用队列来实现线程间的同步

#在python2中导入Queue
from Queue import Queue

#python3中导入
#from queue import Queue

#利用Queue作为管道 进行多个线程间的通信

class Producer(Thread):
	def run(self):
		global queue;
		count = 0;
		while True:
			if queue.qsize()<1000:
				for i in range(100):
					count += 1;
					msg =self.name+"生成产品"+str(count);
					queue.put(msg);
					print(msg);
			time.sleep(1.0);

class Consumer(Thread):
	def run(self):
		global queue;
		while True:
			if queue.qsize()>100:
				for i in range(3):
					msg = self.name + "消费了" +queue.get();
					print(msg);
			time.sleep(1.0);

if __name__ == "__main__":
	queue = Queue();
	for i in range(400):
		queue.put("产品原料"+str(i));

	for i in range(2):
		p = Producer();	
		p.start();

	for i in range(5):
		c = Consumer();
		c.start();


		
		

					











