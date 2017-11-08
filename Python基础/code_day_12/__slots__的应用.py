#coding=utf-8
class Person(object):
	# __slots__ 声明一个元组，元组内声明字符串为其约束变量名称 ，为声明的变量名称不能添加

	__slots__ = ("name","age");
	
	def __init__(self,newName,Age):
		self.name = newName;
		self.age = Age;

p = Person("a",100);
p.sex = "FFF";
print(p.sex);
