#coding=utf-8
#类装饰器
class Test(object):
	def __init__(self,func):
		print("init");
		print("func name is %s"%func.__name__);
		self.__func = func;
	
	def __call__(self):
		print("装饰器");
		self.__func();


print("利用类的调用顺序和python若类型的特点，达到装饰器的目的")
#首先会创建Test类的实例对象，并且吧test这个函数名传递到__init__中去，并且在Test对象中__func变量指向了这个test函数体
#test函数相当于指向了Test创建出来的实例对象
#当在使用test() 进行调用时，就相当于让该对象进行（），继而会调用该对象__call__方法 ，利用这一特性，重写__call__ 并在其内部从新调用func方法，




#相当于 test = Test(test); 调用结束后test指向的是Test（test）返回的对象，而不是
#test（）函数

@Test
def test():
	print("fooooooo");

test();



