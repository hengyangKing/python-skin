#coding=utf-8
class Money(object):
	def __init__(self):
		self.__value = 10;

	@property
	#@property 装饰器 装饰下面该函数 get方法,直接调用该函数，为相对应的属性，省略getter方法
	def money(self):
		return self.__value;
	
	@money.setter
	def money(self,newValue):
		if isinstance(newValue,int):
			self.__value = newValue;
		else:
			print("不是整数");

	@money.deleter
	def model(self):
		 del self._x


a = Money();

print(a.money);

a.money = 1000;

print(a.money);

del a.money;
print(a.money);


