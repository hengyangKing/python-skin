#coding=utf-8
class Game(object):

	#类属性
	num = 0;

	#实例方法
	def __init__(self,game_name):
		#实例属性
		self.name = game_name;
		print (self.name);

	#使用@classmethod装饰器来创建类方法.
	@classmethod
	def add_num(cls):
		cls.num += 1;



	#使用@staticmethod装饰器来修饰静态方法,静态方法区别于类方法和实例方法的显著区别在于，静态方法可以没有任何参数,静态方法和类&实例没有关系
	@staticmethod
	def printFoo():
		print("print foo");







game = Game("2k18");
#类对象调用类方法
Game.add_num();
print (Game.num);
#实例对象调用类方法
game.add_num();
print (Game.num);


#静态方法的调用
Game.printFoo();#通过类调用静态方法

game.printFoo();#通过实例对象调用静态方法

