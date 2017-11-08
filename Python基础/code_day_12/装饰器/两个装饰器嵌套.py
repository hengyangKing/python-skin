#coding=utf-8
def makeBold(func):
	def warpped():
		print ("--------block1---------");
		return "<b>" + func() + "</b>";
	return warpped;

def makeItalic(func):
	def wapped():
		print ("--------block2---------");
		return "<i>" + func() + "</i>";
	return wapped;

# 相当于二次包装
# @makeItalic  相当于test3 = makeItalic(test3);
@makeBold
@makeItalic
def test3():
	print ("------test3--------");
	return "hello world --- 1";

ret = test3();
print(ret);





