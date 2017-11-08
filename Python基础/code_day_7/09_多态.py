#coding=utf-8
class Dog(object):
	def print_self(self):
		print("--------");

class KaKa(Dog):
	def print_self(self):
		print("********");

def introduce(temp):
	#在调用的一刹那 才决定具体调用父类的方法还是子类的方法，
	temp.print_self();


dog = Dog();
kaka = KaKa();


introduce(dog);
introduce(kaka);


