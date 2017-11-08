#coding=utf-8
def test():
	print("---1-----");
test();#调用函数
print(test); #打印函数得知 test是一个 function类型 的函数块


#什么是闭包
#在函数内部在定义一个函数，并且这个函数用到了外边函数的变量，那么这个函数以及用到的一些变量成为闭包
def test_2(number):
	def test_in(number_in):
		print("in test_in 函数,number_in is %d"%number_in);
		return number+number_in;

	return test_in

ret = test_2(20);

print(ret(100));

print(test_2(111)(222));


print("python 中的闭包 从声明语法上来看和其他语法有明显不同，同样为一个函数，只不过在函数内部声明了一个函数，并将其返回，这样可以方便延时调用");

