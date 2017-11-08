#coding=utf-8
class Animal:
	def eat(self):
		print("eat");
	
	def sleep(self):
		print("sleep");

	def run(self):
		print("run");

#继承自Animal
class Dog(Animal):
	def bark(self):
		print("dog bark");
	#重写父类方法
	def eat(self):
		print("吃骨头");	
class Cat(Animal):
	def catch(self):
		print("cat catch");	
	#重写父类方法
	def eat(self):
		#super() python3中新添加属性  调用父类对象
		super().eat();
		print ("吃罐头");


kaka = Dog();
kaka.eat();
kaka.bark();	

tom = Cat();
tom.eat();
tom.catch();



