#coding=utf-8
#内建属性 既默认拥有的属性，
#Person 继承于object
class Person(object):
	def __init__(self,subject):
		self.subject = subject;
		self.subject2 = "cpp";

	#属性访问时拦截器，访问属性时必须调用该方法，多用于log
	def __getattribute__(self,obj):
		print("====1>%s"%obj)
		if obj == "subject":
			print("object is subject");
			return "hahahahha";
		else:
			return object.__getattribute__(self,obj);

	def show(self):
		print ("this is Person");


man = Person("python");

print(man.__dict__)
print (man.subject)
print (man.subject2)

man.show();

