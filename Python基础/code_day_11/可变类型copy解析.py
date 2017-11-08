#coding=utf-8
import copy
#可变类型的copy解析
#1.直接赋值,其实就是对象的引用(别名), 赋值引用，a 和 b 都指向同一个对象。;
a = [1,2,3];
b = a;
print(a);
print(b);
print(id(a));
print(id(b));
print("-----");



#2.浅copy,拷贝父对象，不会拷贝对象的内部的子对象,a 和 b 是一个独立的对象,但他们的子对象还是指向统一对象（是引用）
a = {1:[1,2,3]}
b = a.copy();
print(b);
a[1].append(4);

print(a);
print(b);
print(id(a));
print(id(b));
print("-----");


#3.深copy 利用copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象,两者是完全独立的.
c = copy.deepcopy(a);
a[1].append(5)

print(a);
print(c);
print(id(a));
print(id(c));
print("-----");





