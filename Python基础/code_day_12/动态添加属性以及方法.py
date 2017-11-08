#coding=utf-8
class Person(object):
	def __init__(self,newName,newAge):
		self.name=newName;
		self.age=newAge;
	

a = Person("a",10);
print(a.name,a.age);
#向一个对象添加一个属性
a.male = True;
print (a.male);


#该类的另外一个对象无法调用其他对象添加的属性
b = Person("b",15);
#print (b.male);


#向该类添加一个属性
Person.brains = 120;
print(a.brains);
print(b.brains);

#向一个实例对象添加一个实例方法 
def walk(self):
	print("%s----------walk"%self.name);

#虽然a对象中walk属性已经指向函数walk 但是，并不会自动传递参数self，既并没有将a当作第一个参数，导致崩溃
#a.walk=walk;
#a.walk();
#这里需要借助types框架,将walk函数和a对象进行绑定，并返回一个函数

import types
a.walk = types.MethodType(walk,a);
a.walk();

#绑定的延伸
xxxxxx = types.MethodType(walk,b);
xxxxxx(); 
