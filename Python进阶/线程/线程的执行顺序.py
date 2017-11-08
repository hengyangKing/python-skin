#coding=utf-8
import threading
import time

class SubThread(threading.Thread):
	def run(self):
		for i in range(3):
			time.sleep(1);
			print("i'm"+self.name+" @ "+str(i)+"\n");

def test():
	for i in range(3):
		t = SubThread();
		t.start();
		#print("-"*50)
if __name__=="__main__":
	test();

