#coding=utf-8
tuple = (1,2,3,4,5,6);
print (tuple);

#元组 相当于const 定义 无法修改

#空tuple
tuple_1 = ();
print (tuple_1);

#只有一个元素的元组 元组中只包含一个元素时，需要在元素后面添加逗号
tuple_2 = (1,)
print (tuple_2);


#修改元组
tuple_3= tuple + tuple_1 + tuple_2;
print (tuple_3);


#删除 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tuple;
print ("-------------");
print tuple;





