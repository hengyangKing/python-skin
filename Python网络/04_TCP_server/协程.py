#coding=utf-8
#协程又名微线程，纤程，Coroutne
#在python中 协程底层相当于一个生成器
import time
def A():
	while True:
		print("---A");
		yield
		time.sleep(0.5);

def B(b):
	while True:
		print("---B");
		b.next();
		time.sleep(0.5);

if __name__ == "__main__":
	#yield 修饰过的函数该函数 会变成一个生成器，会返回一个生成器对象
	B(A());

