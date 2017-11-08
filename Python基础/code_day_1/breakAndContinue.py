# coding=utf-8

# for(int i=8,i<10,i++)
num=raw_input("loop num is:")
chat=raw_input("title is:")
intNum=int(num);
kingfloat=3.141592654

if intNum>0:

	for intNum in xrange(0,intNum):
		print "%s===%d-----%.2f"%(chat,intNum,kingfloat)
		if intNum>5:
			print "intNum>5"
			break;
			# continue;
else:
	print "num cannot is zero"