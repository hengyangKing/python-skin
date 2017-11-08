#coding=utf-8
#1.列表生成式
a = [x for x in range(10)];
print(a);

#生成器
#在某些场景中你会需要一个巨大的列表 但是你并不希望现在就生成这么大的列表，而是你只是希望你只用到其中某几个内容 
#生成器只保存计算出每一个值的方式，而不会先生成，等到需要使用时，再生成

#生成器
#第一种生成方式 将列表生成器[] 改成()tumpe 既
b = (x for x in range(10));
print(b);
#利用next()函数 每次执行生成一个,越界会导致崩溃

print(next(b));

#利用yield关键字 只要添加yield 关键字的函数 则变成一个生成器
#届时 调用该函数则不会执行 而通过 next() 函数执行 在yield处形成一个断点 而yield 后修饰的变量则为生成器的内容
#既 在yield 处断点并将 其修饰的值返回 在next()调用时则顺序继续向下执行
#

def createSeries(num):
	print("start-----");
	a,b = 0,1;
	for i in range(num):
		print("a");
		yield b;
		print("b");
		a,b = b,a+b;
		print("c");
	print("finish-----");


series = createSeries(5);

for i in series:
	print(i);

print ("next(生成器对象) 与 生成器对象.__next__()等价");
