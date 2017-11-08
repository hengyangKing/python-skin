#coding=utf-8
class Aclass:
	def test(self):
		print("test A");

class Bclass:
	def test(self):
		print("test B");

#多继承两个类
class ABClass(Aclass,Bclass):
	pass	

foo = ABClass();
foo.test();
#调用一个方法时 搜索的顺序,若在某个类中搜索到该方法，则调用该方法，
#python3 中提示该方法，python中不存在该算法
print(ABClass.__mro__);
print("c3 算法决定了__mro__内的调用顺序");

