#coding=utf-8
#引用
a = 100;
b = a;

print(id(a));
print(id(b));

a+1;
print ("a + 1 = %d"%a);
print ("b == %s"%b);

A = [1,2,3,4,5];
B = A;

A.append(6);
print (A);


print ("---")

print (B);

print ("B引用A的内存地址,python 中 = 的赋值，统统都是引用");

