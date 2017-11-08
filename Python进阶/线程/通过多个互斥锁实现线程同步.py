#coding=utf-8
from threading import Thread,Lock
import time
#线程同步，按照预订的先后顺序进行运行

class Task1(Thread):
	def run(self):
		while True:
			if lock1.acquire():
				print("Task1---");
				time.sleep(0.5);
				lock2.release();


class Task2(Thread):
	def run(self):
		while True:
			if lock2.acquire():
				print("Task2----");
				time.sleep(0.5);
				lock3.release();


class Task3(Thread):
	def run(self):
		while True:
			if lock3.acquire():
				print("Task3----");
				time.sleep(0.5);
				lock1.release();


if __name__=="__main__":
	lock1=Lock();
	
	lock2=Lock();
	lock2.acquire();

	lock3=Lock();
	lock3.acquire();

	Task1().start();
	Task2().start();
	Task3().start();
	

					



