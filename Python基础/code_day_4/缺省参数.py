#coding=utf-8
def printInfo(name,age=18):
	print ("name is %s"%name);
	print ("age is %d"%age);

#缺省参数 只能放参数的最后，

#调用
printInfo(name = "foo");
printInfo(name = "foooo",age = 22);

printInfo("name",999);
printInfo(None,0);


