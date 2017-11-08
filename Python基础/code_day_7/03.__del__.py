#coding=utf-8
class Person:
	def __del__(self):
		print("********");
		print(self);


tom = Person();#tom 指向 Person()出的对象的内存地址
Jimmy = tom ;#Jimmy 指向tom 指向的对象的内存地址

print (tom);
print (Jimmy);

del tom; #删除tom 对Person()对象的引用 
del Jimmy #删除Jimmy 对Person()对象的引用 
print ("------")



