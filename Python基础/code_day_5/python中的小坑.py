#coding=utf-8

#1.交换变量
num_1 = 100;
num_2 = 200;
print (num_1,num_2);
num_2,num_1 = num_1,num_2;
print (num_1,num_2);

#2.可变数据类型
def test(par):
	par+=par;
	print(par);

a = 100;
test(a);
print (a);
print("不可变数据类型的实际参数 不会随着行参的运算而发生改变")

b = [100];
test(b);
print (b);
print ("可变数据类型的实际参数 会随着行参的运算而改变")


print("指针指向的数据类型很关键");
