#coding=utf-8
#定义全局变量多建议增加g_
#定义一个全局变量
a = 0;
def set_a():
	#若a这个变量已经在全局变量的位置定义了，此时还想在函数中对这个全局变量进行修改的，那么 a = 88 会被认为是一个局部变量，仅仅认为是一个和全局变量相同名字的局部变量 
	a = 88;
	print ("set_a %d"%a);
	#需要在该变量前添加关键字global ，global 可以在 变量使用后声明该变量
	global a;	
	print ("set_a %d"%a);

def print_a():
	print ("print_a %d"%a);

set_a();
print_a();


