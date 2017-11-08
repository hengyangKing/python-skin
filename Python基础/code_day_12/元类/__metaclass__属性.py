#coding=utf-8
#__mataclass__属性决定 在创建类时谁创建这个类

def upper_attr(class_name,class_parents,class_attr):
	newAttr = {};
	for name,value in class_attr.items():
		if not name.startswith("__"):
			newAttr[name.upper()] = value;
 
	return type(class_name,class_parents,newAttr);

class Man(object):
	#__mataclass__ = upper_attr("Mannnnnnnnn",(),{"Fmale":True});
	__mataclass__ = upper_attr;
	def eat(self):
		print("eat");


jim = Man();
print(jim.__class__);
