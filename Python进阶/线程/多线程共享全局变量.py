#coding=utf-8
import time
from threading import Thread

num = 100;
def work1():
	global num
	for i in range(3):
		num+=1;
		print(num);

def work2():
	global num
	print(num);

def test():
	t1 = Thread(target=work1);
	t1.start();
	
	#time.sleep(1);
	t2 = Thread(target=work2);
	t2.start();

if __name__=="__main__":
	test();
	print(num);

