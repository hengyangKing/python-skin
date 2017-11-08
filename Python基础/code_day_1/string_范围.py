# coding=utf-8
str ="hello world"



# 取某个范围的字符
print "%s"%(str[0:2])
# 从某个下标到最后一位的写法。。。
print "%s"%(str[3:len(str)])
# 从某个下标到最后一位的另一种写法
print "%s"%(str[4:])
# 取出最后三位的方法
print "%s"%(str[len(str)-3:])
# 取出最后三位的另一种方法
print "%s"%(str[-5:])