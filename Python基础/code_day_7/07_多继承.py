#coding=utf-8
class Aclass:
	def printA(self):
		print("printA");

class Bclass:
	def printB(self):
		print("printB");

#多继承两个类
class ABClass(Aclass,Bclass):
	pass

foo = ABClass();
foo.printA();
foo.printB();


