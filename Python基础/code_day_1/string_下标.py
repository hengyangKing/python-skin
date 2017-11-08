# coding=utf-8
# 字符串的索引（下标）
str="hello world"
def forinStr(fooStr):

	for i in xrange(0,len(fooStr)):
		print "%s"%fooStr[i],

	# for i in xrange(0,len(forinStr)):
	# 	print "倒叙输出"
	# 	print "%s"%fooStr[-i],
	i=0
	while i<fooStr:
			print "倒叙输出=%s"%fooStr[-i]
			i+=1
			if i>=len(fooStr):
				break;

print "str==%s"%str
# 字符串处理
# 取下标
index=input("index=:")

if index<=len(str):
	subStr=str[index]
	print "subStr==%s,index==%d"%(subStr,index)

else:
	print "超出str长度"
	forinStr(str)