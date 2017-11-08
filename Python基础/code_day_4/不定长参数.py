#coding=utf-8
# *修饰的行参具有特殊的功能
# *修饰的行参必须放在所有的行参的最后


def sumNums(*args):
	print(args);


def sumNums_2(a,b,*args):
	print (a);
	print (b);
	print (args);


sumNums(1,2,3,4,5,6,7,8,9);

sumNums_2(1,2,3,4,5,6,7,8,9,0);

#未给args赋值，其为一个空元组
sumNums_2(100,200);



def sumNums_3(a,b,c=10,*args,**kargs):
	print (a);
	print (b);
	print (c);
	print (args);
	print (kargs);
#传递多余参数之前不带变量名，都传递进*修饰的行参内 以元组方式保存
sumNums_3(1,2,3,4,5,6,7,8,9,0);

#传递多余参数之前不变量名，都传递进**修饰的行参内 以字典方式保存
sumNums_3(20,30,40,50,name = "king",age = 998,famal = False);

