#coding=utf-8
#init 方法
class Person:
	def eat(self):
		print("eat");
	def sleep(self):
		print("sleep");

	#1.创建一个对象
	#2.解释器自动调用_init__方法
	#3.返回创建对象的引用
	def __init__(self):
		print("重写__init__方法");
		self.Famal=True;

		



tom = Person();
tom.eat();
tom.sleep();
print(tom.Famal)
	
