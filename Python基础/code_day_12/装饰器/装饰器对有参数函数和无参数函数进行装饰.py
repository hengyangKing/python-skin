#coding=utf-8

#无参数
def Decorator(funcName):
	print("Decorator----");
	funcName();
	def func_in():
		print("func_in-----");
		funcName();
		print("func_in2----");
	return func_in;
@Decorator
def test():
	print("-----test-----");

test();

print("-"*100);
#有参数
def Decorator2(func):
	print("Decorator2------")
	def func_in(*argc,**kargc):
		func(*argc,**kargc);

	return func_in;

@Decorator2
def test2(a,b,c,d,e):
	print(a,b,c,d,e);

test2(1,2,3,4,5);
	
print ("*"*90)
#有返回值
def Decorator3(func):
	def func_in():
		ret = func();
		return ret;
	return func_in;

def test3():
	print ("test3------");
	return "hahha";
print ("test3 return value is %s"%test3());
