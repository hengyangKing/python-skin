#coding=utf-8
#自定义异常类型

class ShortInputException(Exception):
	#自定义异常类，继承于Exception
	def __init__(self,length,atleast):
		self.length = length;
		self.atleast = atleast;


def main():
	try:
		s = input("请输入--->");
		if len(s) < 3:
			#raise 触发异常
			raise ShortInputException(len(s),3);
	except ShortInputException as res:
		#res 这个变量呗绑定到了错误的实例
		print("ShortInputException 输入的长度是 %d 长度应该是 %d"%(res.length,res.atleast));
	else:
		print("没有异常发生");
	
	finally:
		print("无论如何都执行了");
		
main();
