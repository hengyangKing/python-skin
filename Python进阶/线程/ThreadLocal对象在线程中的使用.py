#coding=utf-8
#使用局部变量的时候，需要传递参数，比如有这样一个例子，程序需要处理客户申请，每来一个客户，就新开一个线程进行处理，而客户有姓名、年龄、性别等属性（参数），如果都需要传递参数的话很繁琐。Python提供了threading.local模块，方便我们实现线程局部变量的传递。


import threading
#创建全局threadlocal对象

local = threading.local();

def student():
	global local;
	print ("hello ,%s (in %s) \n"%(local.student,threading.current_thread().name));


def process_thread(name):
	local.student = name;
	student();

t1 = threading.Thread(target = process_thread,args=("A",),name="Thread-----A");
t2 = threading.Thread(target = process_thread,args=("B",),name="Thread-----B");

t1.start();
t2.start();


print("可见，每个线程都可以对threading.local对象进行读写，且互相不干扰。合理使用threading.local可以极大简化代码逻辑，同时保证各个子线程的数据安全。Threading.local最大的用处就是HTTP请求时绑定用户的信息，这样每个用户线程可以非常方便访问各自的资源而互不干扰。")
