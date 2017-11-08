#coding=utf-8
#functools 一些工具函数放在 该包内
import functools
#print (dir(functools));


#函数的描述
def note(func):
	"i'm func note describe"
	@functools.wraps(func)
	def wrapper():
		"wrapper func"
		print("note something");
		return func();
	return wrapper;


@note
def test():
	"i'm func test describe"
	print ("i'm test");

print(help(test));


