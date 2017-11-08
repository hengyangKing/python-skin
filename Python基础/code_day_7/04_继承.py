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
	
class Cat(Animal):
	def catch(self):
		print("cat catch");	

kaka = Dog();
kaka.eat();
kaka.bark();	

tom = Cat();
tom.eat();
tom.catch();



