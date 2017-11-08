#coding=utf-8
# == is
a = [1,2,3];
b = a;
print (a == b);

print (a is b);


c = [1,2,3];
print (a == c);
print (a is c);



d = copy.deepcopy(a);
print (a == d);

print (a is d);

print ("is 是用来判断是否指向同一块内存引用 == 判断所指向的内存的内容是否相同")
