#coding=utf-8
#生成器对象
def test():
	i = 0;
	while i<10:
		print("------------1------------")
		temp = yield i
		print("------------2------------")
		print(temp);
		i += 1;
		print("------------3------------")
	

	print("-----finish");


foo = test();
for i in range(9):
	#next(foo);
	#初次调用send() 会导致崩溃 因为初次运行时 执行卡在yield i 并没有给temp一个返回值 send 也无从赋值，导致崩溃 
	if i == 0:
		foo.send(None);

	foo.send("hhhhhh");
print("send(xxxx)和next都能使生成器进行下一次的值，不同的是 send是可以将 yield x的返回值进行包装 也就是说将迭代器的返回值进行修改")

print

	
