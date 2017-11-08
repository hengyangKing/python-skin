#coding=utf-8
try:
	11/0;
	open("xxx.txt");
	print("error_1---");
	print(num);
	print("error_2---");
except (NameError,FileNotFoundError):
	print ("NameError");
	print ("FiLL NOT FOUND ERROR");
except Exception as ret:
	print("若使用Exception ，那么意味着只要上面的except没有捕获到异常，这个Except 一定会捕获到，其为所有异常的总称");
	print (ret); #as 关键字后跟异常真实参数 
else:
	print("没有异常才会执行的功能");
finally:
	print("无论是否有异常都会执行");
print ("123");
