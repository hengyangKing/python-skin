#coding=utf-8
from threading import Thread
import time

class SubThread(Thread):
	def run(self):
		for i in range(3):
			time.sleep(1);
			print("i'm"+self.name+" @ "+str(i));




if __name__ == "__main__":
	subT = SubThread();
	subT.start();


print("ff000000")
