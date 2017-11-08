#coding=utf-8
import os

folder_path = raw_input("请输入需要重命名的文件夹的路径:\n");
folder_path+="/";

os.chdir(folder_path);

file_names = os.listdir(folder_path);

i = 0;
while i<len(file_names):
	file_name = file_names[i];
	os.rename(file_name,str(i)+"-"+file_name);
	i+=1;

