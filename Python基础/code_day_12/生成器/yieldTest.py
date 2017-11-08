#coding=utf-8
def createSeries(num):
	print("start-----");
	a,b = 0,1;
	for i in range(num):
		print("--------------a");
		yield b;
		print("--------------b");
		a,b = b,a+b;
		print("--------------c");
	print("finish-----");



