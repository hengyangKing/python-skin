#coding=utf-8
class Person:
	#类的私有属性
	#__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
	def __init__(self):
		self.__age = 0;		


	def setAge(self,newAge):
		if newAge>0 and newAge<=130:
			self.__age = newAge
		else: 
			self.__age = 0;	
		self.__printLine();

	def age(self):
		self.__printLine();
		return self.__age;

	

	#类的私有方法
	#__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 
	def __printLine(self):
		print("----------------------------------------");



tom = Person();
tom.setAge(-10);
print(tom.age());

tom.setAge(100);
print(tom.age());


