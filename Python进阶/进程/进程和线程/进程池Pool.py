#coding=utf-8
#进程池Pool

from multiprocessing import Pool
import os,time

def worker(msg):

	print("%s开始执行，进程号为%d"%(msg,os.getpid()));
	time.sleep(1);

#定义一个进程池，最大进程数3
po = Pool(3);

for i in range(10):
	#pool.apply_async(要调用的对象，传递给目标参数的元组)；
	#异步添加worker调用进入进程池
	po.apply_async(worker,(i,))

print("start");
#关闭进程池，相当于不能够再次添加新的任务
po.close();
#主进程创建添加，任务后，主进程默认不会等待进程池中的任务执行完成后才结束
#而是当主进程的任务完成之后直接结束，若是不调用join 会导致进程池中国的任务不会执行
po.join();
print("end");



