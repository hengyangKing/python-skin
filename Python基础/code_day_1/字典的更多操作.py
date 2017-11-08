# coding=utf-8
# 字典的更多操作
info={"name":"king","age":18,"address":""}

# 1.len()函数 打印字典内的key的个数
print len(info);


#2.keys() 对象函数 返回字典内所有的key值的列表

print info.keys();

#3.values 对象函数 返回字典内所有的value的列表
print info.values();

#4 items 返回数组 所有包含的key value的单对应字典
print info.items();

#5 has_key("fooooo") 减少了许多if in 带来的不便利
print info.has_key("name")
