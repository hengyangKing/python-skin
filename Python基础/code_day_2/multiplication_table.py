#coding=utf-8
#num =round(float(raw_input("请输入你想看到的阶数/n")));
num = 9;
i = 1;
while i<=num:
	j = 1 
	while j<=i:
		print (" %d x %d = %d\t"%(j,i,i*j),end="")
		j+=1

				
	print ("");
	i+=1;
