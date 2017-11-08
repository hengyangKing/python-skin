#coding=utf-8
a = '==='
b = '---'
c = 'abc'
d = a+b+c;
print d
e = '++++++'+a+'********'+b+'44444'+c
print e 
f = '!!!!!!!!%s!!!!!!!!!'%(a+b+c+d)
print f



name = 'abcdefABCDEF'
print 'name is %s'%name
#rang 并不是起始下标 & 长度 而是起始下标--->终止下标，从左至右
subName = name[2:5]
print "name[2:5]"+subName;
#终止下标为负数时 从该字符串倒数第一位开始取
subName_2 = name [2:-1];
print 'name [2:-1]'+subName_2

#至末尾不填写结束下标参数,自动找到截至点
subName_3 = name [2:];
print ' name [2:]'+subName_3;

#设置过滤步长
subName_4 = name [2:6:2];
print 'name [2:6:2]'+subName_4;

#倒序
subName_5 = name [-1:0];
print 'name [-1:0]'+subName_5;

#结果为空因为起始点-1 ，从左到右,通过修改步长得到答案
subName_6 = name [-1:0:-1];
print 'name [-1:0:-1]'+subName_6;

#截止点为0 并不包括第0位  sososo 不填写参数，为默认截止点
subName_7 = name [-1::-1];
print 'name [-1::-1]'+subName_7;









 


