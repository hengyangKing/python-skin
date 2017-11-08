#coding=utf-8
str = 'hello world'

#find 
print (str.find("world"))
print (str.find("king"))

print "------------------------"
#index 
print (str.index("world"))
#print (str.index("king"))

print "------------------------"
#count 
print (str.count("l"));

print "------------------------"
#replace 
print (str.replace("e","E"));
print str;
print "------------------------"
#更改替换个数
print (str.replace('l','L',2))
print str;

print "------------------------"
#split 关键词分割 返回列表 
print (str.split(" "));
print str;
print "------------------------"

#capitalize() 字符串首字母大写
print (str.capitalize());

print "------------------------"

#title 单词首字母大写
print(str.title());

print "------------------------"
#endswith() 结尾判断
print (str.endswith('.txt'));

print "------------------------"
#startswith()
print (str.startswith('http'));

print "------------------------"
#lower
print (str.lower());

print "------------------------"
#upper
print (str.upper());

print "------------------------"
#rjust
print (str.rjust(50));

print "------------------------"

#center 
print (str.center(50));

print "------------------------"

#ljust
print (str.ljust(50));

print "------------------------"
#lstrip rstrip strip  删除两边空格
print (str.strip());

print "------------------------"
#partition() 关键词分割 返回元组 
print (str.partition("hello"))
print str;
print "------------------------"
