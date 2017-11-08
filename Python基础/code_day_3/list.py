#coding=utf-8
#py中的list 区别于数组的地方在于可以存放不同数据类型的数据

nums= [1,2,3,4,5,6,7,8,9];

print nums;
print "-------------------"

#增
#append 
nums.append(10);
print nums;

print "-------------------"

#insert
nums.insert(0,0);
print nums;

print "-------------------"

#extend() 合并
nums_1=[11,12,13];
nums.extend(nums_1);
print nums;

print "-------------------"
#+
nums_2 =nums+nums_1;
print nums_2;

print "-------------------"

#删
#pop()
nums.pop();
print nums;
print "-------------------"


#remove() 参数必须为list 内存在的数据 否则崩溃
nums.remove(10);
print nums;
print "-------------------"


#del
del nums[5];
print nums;
print "-------------------"


#改
nums[0]=1000000;
print nums;
print "-------------------"




#funs
if 2 in nums:
	print '2 in nums'


if 999 not in nums: 
	print '999 notin nums'


