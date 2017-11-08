#coding=utf-8
import os
import time
g_num = 10;

ret = os.fork();
if ret == 0:
	print ("sub process");
	g_num += 1;
	print("in sub process num is %s"%g_num);
else:
	print ("main process");
	#保证子进程一定先执行
	time.sleep(3);
	print("in main process num is %s"%g_num);


print("不同的进程数据相互独立，进程间的变量互不影响，")
