#coding=utf-8
from threading import Thread
import time

def test():
	print("foo");
	time.sleep(1);


for i in range(4):
	t = Thread(target=test);
	t.start();
