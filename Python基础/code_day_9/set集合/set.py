#coding=utf-8
a_tuple=(11,22,33,11,22,33);
print(a_tuple);

b_list = [11,22,33,11,22,33];
print(b_list);

c_set = {11,22,33,11,22,33};
print(c_set);

print("set在python 2 和  3 显示方式不同 set不允许有重复项")

#将 tuple set化
d_set =set(a_tuple);

print(d_set);










'''
python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.  
  
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。  
'''


