#coding=utf-8
import time
#fork 函数不跨平台不能用于windows  跨平台方案应该调用其底层类 创建一个进程对象
from multiprocessing import Process
def test():
	while True:
		print("sub process")
		time.sleep(1);

#创建子进程对象,参数为子进程需要执行的代码,test 调用完成后意味该进程执行结束
process1 = Process(target=test);
process1.start();


print("main process");
'''while True:
	print("main process");
	time.sleep(1);
'''
