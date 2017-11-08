#coding=utf-8

#lambda 声明的匿名函数

infos = [{"name":"z","age":10},{"name":"n","age":99},{"name":"z","age":00}];

infos.sort(key=lambda x:x["name"]);
print (infos);

infos.sort(key=lambda x:x["age"]);
print (infos);


def lambdaFunc(a,b,func):
	return func(a,b);
#lambda 声明一个匿名函数 lambda函数的语法只包含一个语句，如下：
#lambda [arg1 [,arg2,.....argn]]:expression

print (lambdaFunc(1,2,lambda x,y:x+y));

#声明匿名函数为变量
sum = lambda arg1,arg2 :arg1*arg2;
print("sum func %s"%sum(10,10));



func_new = eval(input("请输入一个匿名函数:\n"));
print (lambdaFunc(5,8,func_new));

