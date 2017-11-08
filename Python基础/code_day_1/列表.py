# coding=utf-8
# 列表类型变量 

foo=["foo1","foo2","foo3","foo4"]
print foo

# 列表类似于c中的数组  但是区别在于可以存储不同类型的数据 更像是NSArray 
for i in xrange(0,len(foo)):
	print foo[i]
print "..................."



# for枚举用法
for j in foo:
	print "---foo %s"%j


# 列表的遍历
names=["dlsandnas",dsakdasdsa,"nsdkjnsandksankdnsak","ndkanskdnka","nskda"]
i=0
while i<len(names):
	print "name %s is %s"%(i,names[i])
	i+=1



