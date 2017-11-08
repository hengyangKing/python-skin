# coding=utf-8
# 字典的增删改查
info={"name":"king","age":18,"address":"大台子9号"}

print info

# 修改元素
# newName=raw_input("请输入新的姓名:")
# if "name" in info:
# 	info["name"]=newName;

# print info

#新增元素
if "newElement" in info:
    print "不存在"
else:
	info["newElement"]="foooooooo"
	print info
# 即key存在则修改 key不存在则新增


# 删除 del clear
# del info["address"]
# print info

# 清除字典内所有的key value
info.clear()
print info

# 查询
# 遍历查询
# 根据key查询







