#coding=utf-8
def Decorator(func):
	def func_in(*args,**kargs):
		return func(*args,**kargs)
	return func_in;

@Decorator
def test():
	print("test");

@Decorator
def test1():
	print("test1");
	return "hahaha";

@Decorator
def test2(a):
	print("test2 a = %d --- "%a);

test();
print(test1());
test2(123);
 
