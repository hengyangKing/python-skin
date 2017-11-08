# coding=utf-8
#列表的常见操作

names=["names0","names1","names2","names3","names4","names5","names6","names7"]
print "names is %s"%names

#新增项目 append()
# newName=raw_input("places input a New name :")
# names.append(newName)
# print "names is %s"%names

#更改直接替换

# the_newName=raw_input("pleace input a newName with names0:");
# # names[0]=the_newName;
# print "*"*30
# print "names is %s"%names

# #查找列表内的相关内容 if in 函数
# if the_newName in names:
# 	print "该名称已经存在于列表内，请从新输入"
# 	the_newName=raw_input("place input a newName with names0:");
# else :
# 	names[0]=the_newName;



#删除 根据下标 del names[index]
num=raw_input("pleace input your want delete Name index:")
if int(num)<=len(names):
	del names[int(num)]
	print "names is:%s"%names
else :
	print "the index beyond the mark"


#删除 pop函数 相当于出栈 names.pop()

names.pop()
print "---"*30
print "names is:%s"%names

#删除 remove函数 remove(对象)

print "---"*30
names.remove(names[3])
print "names is:%s"%names


