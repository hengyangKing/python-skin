#coding=utf-8

def w1(func):
	def inner():
		print("正在验证权限");
		func();
	return inner;

# 在函数声明前  添加@w1  效果等价于 func = w1(func);
@w1
def func():
	print("我是函数func");

@w1
def func2():
	print("我是函数func2");
#将func 所指向的函数指针 指向闭包所返回的函数，并在闭包内调用传入的参数函数,这样不改变函数的调用方式，并对该函数进行包装的方法叫装饰器 
#func = w1(func);
#func();


func();
func2();


