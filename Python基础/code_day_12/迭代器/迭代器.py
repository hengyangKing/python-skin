#coding=utf-8
#迭代器 
#迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置的对象，迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束，迭代器只能向前不会后退


#可迭代的对象
#以直接作用于for循环的数据类型有以下几种
#集合数据类型：list，tuple，set，str，dic

#框架测试是否为可迭代对象
from collections import Iterable

print(isinstance("a",Iterable));




