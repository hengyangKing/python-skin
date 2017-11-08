#coding=utf-8
#通过gevent 实现多任务 gevent 相当于对greenlet 进行的二次封装，省去了手动调用事件的过程（switch）
import gevent
def f(n):
	for i in range(n):
		print(gevent.getcurrent(),i);
		#用来模拟一个耗时操作
		gevent.sleep(1.0);
g1 = gevent.spawn(f,5);
g2 = gevent.spawn(f,6);
g3 = gevent.spawn(f,7);

g1.join();
g2.join();
g3.join();

print("由此看出 gevent 同时join 3 个协程 执行同一个函数  ")

