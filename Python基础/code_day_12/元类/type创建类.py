#coding=utf-8
class Test(object):
	pass
t1 = Test();
#type(类名，由父类名称组成的元组（针对继承的情况可为空），包含的属性的字典，（名称和值）);
Test2 = type("Test2",(),{}); 
t2 = Test2();

print (type(t1));
print (type(t2));
print (type("Test3"));
