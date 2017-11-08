# coding=utf-8
# 1）.两个字符串是否相等（python中弱化指针的概念 而直接对内存中的值进行操作，相对比较简便）
# a="abc"
# b="abc"
# # 仅对内容进行对比而不是对指针地址进行判断相当于isEquleTo
# if a==b:
# 	print "hahaha"

str="hello King King King King"

# 2）.find 查找是否包含字符串
# （若包含返回目标字符串在被查找字符串中第一次出现的首字母下标，不包含则返回－1)
# str.find("King") 
# 查找某范围内是否包含该字符
str.find("King",0,len(str))



# 3).index 和find类似的查找字符串
str.index("King")#和find不同的是index不包含直接报错而不是返回-1
str.index("King",0,len(str))


#4).count 统计字符串内个数某目标字符的个数,同样可以添加范围
str.count("King")
str.count("King",0,len(str))


#5).len()函数 统计字符串的长度
len(str)

#6).replace() 替换(注意replace不对初识函数进行修改，而是讲替换过后的str在返回值中返回)
str.replace(old, new[, max])
# old -- 将被替换的子字符串。
# new -- 新字符串，用于替换old子字符串。
# max -- 可选字符串, 替换不超过 max 次
str.replace("King","king",3)





#7).split 以某字符串为分隔符将目标字符串切片 如果maxsplit有指定值，仅分割maxspint个字符串
# split 返回值为array
# 'hello king king King King'
# >>> str.split("King",2)
# ['hello ', ' ', ' King King']



#8).capitalize() 把字符串的第一个字符大写

#9).startswith() 检查字符串是否已xxx开头 返回bool

#10).endswith() 检查字符串是否已xxx结尾 返回bool

#11).lower() 将大写字母全部转换成小写字母

#12).upper() 将小写字母全部转换成大写字母

#13).ljust(width) 返回一个文字内容与原字符串相同且左对齐， 并使用空格填充至长度width的新字符串
# 若width小于目标字符串长度，则返回字符串和原字符串相同不进行填充不进行截取

#14).rjust(width) 与上同理

#15).center(width) 与上同理

#16).lstrip() 删除左边的空格 ＃strip 剥去 剥离

#17).rstrip() 删除右边的空格 

#18).rfind() 类似于find( )函数 从右边开始查找

#19).rindex( )类似于index( )函数 从右边开始index

#20).partition(substr) 把目标字符串已substr分割成三部分，substr前，substr，substr后 返回值为元祖类型tuple 
# 注意若是目标字符串中有多个substr则从左边开始第一个开始分隔,和split不同，split不会返回被切割内容，partition则返回被切割内容

#21).rpartition() 同上，从右边开始第一个分隔

#22).splitlines() 处理换行符 split 切割 lines 按照换行符\n分隔目标字符串，返回一个包含各行作为元素的列表
#  str="hello wor \n ld"
# >>> str
# 'hello wor \n ld'
# >>> print "%s"%str
# hello wor 
#  ld
# >>> str.splitlines()
# ['hello wor ', ' ld']


# 23）.isdigit()  digit数字  看目标字符串是否全是数字 返回bool


# 24）.isalpha() 判断字符串是否是纯字母字符串

# 25）.isalnum() 判断目标字符串都是字母或数字返回ture 可用于查看是否有符号

# 26）.isspace() 判断是否全为空格

# 27).isupper() 判断是否为纯大写字符串

# 28）.islower() 判断是否为纯小写字符串

# 29).join(sequence) 用于将序列中的元素以指定的字符连接生成一个新的字符串。

# 注意几种用法。。。

>>> str="_"
>>> li=["hello","world"]
>>> str.join(li)
'hello_world'

>>> str="King"
>>> str.join("***")
'*King*King*'

str = "-";
seq = ("a", "b", "c"); # 字符串序列
'a-b-c'



































