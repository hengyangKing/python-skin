#coding=utf-8
info = {"name" : "king","age" :19 ,"addr": "平乐园" }

print (info);
print ("------------------------")

#key
#python 中的key 不局限于str,像tuple 等不可变类型统统可以成为key 而像list dic等可变类型均不能为key
info[(22,)]=(22,333,222);
info[100]=3.14;
print(info);
print ("------------------------")










#增
info["massage"]=1868888888;
print (info);
print ("------------------------") 


#改
info["name"]="nima--wang";
print (info);
print ("------------------------") 

#删
del info["massage"];
print (info);
print ("------------------------") 


#查
name = info["name"];
print (name);
print (info);
print ("------------------------") 


#get()
sex = info.get("sex");
print (sex);


#常见操作
#len()
print(len(info)); 
print ("------------------------") 


#keys()
keys = info.keys();
print (keys);

print ("------------------------") 


#values()
values = info.values();
print (values);
 
print ("------------------------") 

#items()
items = info.items();
print (items);
print ("------------------------") 

for temp in info.items():
	print(temp);
print ("------------------------") 

