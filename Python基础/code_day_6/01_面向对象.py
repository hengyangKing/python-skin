#coding=utf-8
class Person:
	#func
	def eat(self):
		print("eat");
	
	def sleep(self):
		print("sleep");
	
	def printInfo(self):
		
		print(self.age);
		print(self.name);

	#property
	

man = Person();
man.eat();
man.sleep();

#man.printInfo();


#添加属性
man.age = 18;
man.name = "tom";

man.printInfo();



#print (man.age);
#print (man.name);

	
