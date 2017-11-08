#coding=utf-8
import sys
#导入sys模块 变量argv接收运行时参数
argv = sys.argv;
print (argv);

pyName = argv[0];

print (pyName);

if len(argv)>1:
	for par in argv:
		if par!=pyName:
			print (par);



