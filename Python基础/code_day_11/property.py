#coding=utf-8
class Test(object):
	def __init__(self):
		self.__num = 100;
	

	def setNum(self,newNum):
		print("...set...");
		if newNum >0 and newNum < 100:
			self.__num = newNum;
	
	def getNum(self):
		print("...get...");
		return self.__num;
	

	#利用property函数包装包装set & get 方法 并返回给属性num
	
	num = property(getNum,setNum);
	
	
	def delNum(self):
		print("...del...")
		del self.__num;


	#property 函数还可以同时包装del & doc -- 属性描述信息
	
	num = property(getNum, setNum, delNum, "I'm the 'num' property.")


test = Test();

print(test.num);

print("*"*50);

test.num = 99;

print(test.num);

del test.num;

 
