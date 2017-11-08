#coding=utf-8
import time
#fork 函数不跨平台不能用于windows  跨平台方案应该调用其底层类 创建一个进程对象
from multiprocessing import Process
def test():
	for i in range(5):
		print("sub process i ======%s"%i)
		time.sleep(1);

#创建子进程对象,参数为子进程需要执行的代码,test 调用完成后意味该进程执行结束
process1 = Process(target=test);
process1.start();

#和fork不同的是，fork在主进程结束后该程序就会结束，在命令行中可以进行其他操作，而Process 产生的子进程  主进程不会执行完成后就立刻结束程序，而是在子进程调用结束后再结束程序


print("main process");
'''while True:
	print("main process");
	time.sleep(1);
'''
