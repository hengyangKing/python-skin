#coding=utf-8
class Cat:
	def __init__(self,name,isFamal):
		if isFamal:
			self.sex="girl"
		else:
			self.sex="boy";
		self.name=name;
	
	def eat(self):
		print("%s is eat"%self);
	

	def sleep(self):
		print("%s is sleep"%self);



tom = Cat("tom",False);
tom.eat();
tom.sleep();
print (tom.name);
print (tom.sex);
