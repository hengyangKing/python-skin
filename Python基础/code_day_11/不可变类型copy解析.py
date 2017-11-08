#coding=utf-8
import copy
#1.不可变类型浅copy，同可变类型不同， 相当于赋值
a = [1,2,3];
b = [4,5,6];
c = (a,b);
print(id(c))
print(c);
d = copy.copy(c);

print(id(d));
print(d);

a.append(666);
print(c);
print(d);


#2.deepcopy 深copy 同可变类型相同 都是开辟出两块独立的内存空间 
d = copy.deepcopy(c);
print(id(d));
print(d);

a.append(888);
print(c);
print(d)




