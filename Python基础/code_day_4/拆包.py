#coding=utf-8
def test(a,b,c=33,*args,**kargs):	
	print (a)
	print (b)
	print (c)
	print (args)
	print (kargs)

A = (44,55,66);
B = {"name":"king","age":18};

test(11,22,33,A,B);

#实际参数 前加* 既为拆包，将元组和字典分别拆开，将其值分拆进参数
test(11,22,33,*A,**B);

