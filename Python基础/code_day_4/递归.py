#coding=utf-8
def getRecursiveSequence(num):
	if num>1:
		return (num * getRecursiveSequence(num-1));
	else:
		return num;
	


relust = getRecursiveSequence(02);
print relust;

