#coding=utf-8
#使用range 可以快速返回一个列表 range()语法类似于切片

#range 有内存溢出风险，产生过大长度的列表会导致崩溃，
#1.列表生成式
#生成一个从1到199 步长为2的列表 在list [ ]内 左边声明变量 右边写for循环 不带:
list_1 = [i for i in range(1,200,2)];
print (list_1)

#相当于该语法糖后半部分只控制循环次数和返回变量 语法糖自己负责将返回的变量 add
list_2 = [10 for i in range(0,99,30)];
print (list_2);



#2.带if的列表生成式 只返回满足if条件判断满足的参数
list_3 = [i for i in range(1,100) if i%2==0]
print (list_3);

#3.range 的嵌套 形成矩阵
list_4 = [(i,j) for i in range(3) for j in range(2)];
print (list_4);

