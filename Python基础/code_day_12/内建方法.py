#coding=utf-8
#1.range() 
#列表生成式 
a = [ x*2 for x in range(0,10,2)];
print(a);
#生成器
b = (x*1.5 for x in range(0,20,2));
print (b)
for i in b:
	print (i)

print("*"*50);
#2.map() map函数会根据提供的函数对指定的序列做映射
#map(func,sequence[,,,,,,,,])---->list
#func 是一个函数名，sequence是一个或多个序列，取决于func需要几个参数
#map()函数带一个返回值，为list list的内容取决于函数调用的返回值
def func(a):
	print (a);
	return a*a;
c = map(func,a);
print(c)

d = map(str,a);
print(d);
e = map(lambda x,y:x+y,[1,2,3],[1,2,3]);
 
print(e);

#3.filter filter函数会对指定序列过滤操作 filter(func or None,sequence)->list tuple or string
#filter 函数会对序列参数sequence中的没个元素调用function函数，最后返回的解惑包含调用结果为true的元素
f = filter(lambda x:x%2,[1,2,3,4]);
print(f);


g = filter (None,"hello word");
print(g)

#4.reduce 函数荟萃参数序列中元素进行积累
'''
def f(x):
...     return x * x

再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''


