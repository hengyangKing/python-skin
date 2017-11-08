#coding=utf-8
#利用greenlet 框架实现多任务
# http://blog.csdn.net/shuaijiasanshao/article/details/51475571
#greenlet是python的并行处理的一个库。 python 有一个非常有名的库叫做 stackless ，用来做并发处理， 主要是弄了个叫做tasklet的微线程的东西， 而greenlet 跟stackless的最大区别是greenlet需要你自己来处理线程切换， 就是说，你需要自己指定现在执行哪个greenlet再执行哪个greenlet。

from greenlet import *

def test1():
	print("1");
	gr2.switch();
	print("2");

def test2():
	print("3");
	gr1.switch();
	print("4");

gr1 = greenlet(test1);
gr2 = greenlet(test2);

gr1.switch();
print("最后一行跳转到 test1() ，它打印1，然后跳转到 test2() ，打印3，然后跳转回 test1() ，打印2，然后 test1() 就结束，gr1 dead。这时执行会回到原来的 gr1.switch()")
