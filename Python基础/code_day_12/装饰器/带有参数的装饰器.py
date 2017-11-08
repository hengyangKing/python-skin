#coding=utf-8
def Decorator(pre="hello"):
	def timeFunc(func):
		def warppedFunc():
			print("%s called at %s"%(func.__name__,pre));
			return func();
		
		return warppedFunc;
	return timeFunc;

#装饰器带参数在原有装饰器的基础上，设置外部变量 @Decorator("hahahahha")调用后相当于传递进入参数并返回装饰器闭包本身 相当于@timeFunc只不过多传递进入一个参数待用 
#1先执行Decorator("haahaha") 这个函数，返回timefunc这个函数的引用
#2@timefunc
#3使用@timefunc对foo函数进行装饰
@Decorator("hahahahha")
def foo():
	print ("i am foo");

foo();
