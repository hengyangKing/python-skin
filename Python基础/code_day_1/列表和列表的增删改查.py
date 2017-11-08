# coding=utf-8
# 列表类型变量 

foo=["foo1","foo2","foo3","foo4"]
movies=["坑爹","坑爹","坑爹","坑爹","坑爹","坑爹","坑爹","坑爹","坑爹"]


print foo

# 列表类似于c中的数组  但是区别在于可以存储不同类型的数据 更像是NSArray 
for i in xrange(0,len(foo)):
	print foo[i]
print "..................."



# for枚举用法 直接枚举出的列表元素存在临时变量j中 而不是下标

for j in foo:
	print "---foo %s"%j
print "..................."



movieNumNames=[]
for x in xrange(0,len(movies)):
	movieName=movies[x]+str(x)
    movieNumNames.append(movieName)
	print movieName

print movies
	

	








