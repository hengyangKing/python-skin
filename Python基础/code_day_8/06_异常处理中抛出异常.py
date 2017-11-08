#coding=utf-8
#异常处理中抛出异常
class Test(object):
	def __init__(self,switch):
		self.switch = switch;
	def calc(self,a,b):
		try:
			return (a/b);
		except Exception as result:
			if self.switch :
				print("捕获开启，已经捕获到异常");
				print (result);
			else:
			#重新抛出这个异常，此时就不会呗这个异常处理给捕获到，从而会触发默认的异常处理
			#raise 后跟自定义异常，可触发异常 无自定义异常，则抛出默认异常 
				raise


a = Test(True);
a.calc(11,0);
print ("--------");
a.switch = False;
a.calc(10,0);

 
