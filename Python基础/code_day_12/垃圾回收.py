#coding=utf-8
#垃圾回收
#小整数对象池
#python 对于小整数「-5，256」这些整数对象是提前简历好的，不会被垃圾回收，所以这些整数使用的是同一个对象
a = 100;
b = 100;
print(id(a));
print(id(b));

#大整数对象池
#每一个大整数，均创建一个新的对象


#intern (共享机制),普通字符构成的字符串 同小整数相同同用一份，但是包含空格等特殊字符 的不会共用

c = "hello%%word";
d = "hello%%word";

e = "hello";
f = "hello"

print(id(c));
print(id(d));

print(id(e));
print(id(f));




