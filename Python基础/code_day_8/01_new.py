#coding=utf-8
class Dog(object):
	#python 中 __new__ 方法负责创建
	def __new__(cls):
		#cls此时指向的Dog指向的那个类对象
		print(id(cls));
		print(cls);
		print("9999")
		#调用super __new__ 来创建对象，然后变量dog来接收__new__的返回值，这个返回值表示创建出来的对象的引用 
		#调用super __new__ 来创建对象，自动调用__init__方法

		return object.__new__(cls);
	#python 中__init__方法负责初始化
	def __init__(self):
		print(self);
		print("nnnnn");		

	#python 中这两个方法的组合类似于其他语言中的构造方法
		
dog = Dog();
print(dog);


