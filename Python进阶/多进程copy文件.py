#coding=utf-8
#1.创建一个文件夹
#2.获取源文件夹中所有的名字
#3.多进程copy


import os
from multiprocessing import Pool,Queue

#copy file 
def cpFileTask(name,filePath,newFilePath):

	fr = open(filePath+"/"+name,"r");
	fw = open(newFilePath+"/"+name,"w");
	
	fw.wirte(fr.read());
	
	fr.close();
	fw.close();

def main():

	fileName =str(input("places input fileName:\n"));

	newFileName = fileName + "附件";
	#os.rmdir(newFileName);
	os.mkdir(newFileName);

	fileNames = os.listdir(fileName);

	pool = Pool(5);
	for name in fileNames:
		pool.apply_async(cpFileTask,args=(name,fileName,newFileName));

	pool.close();
	pool.join();

if __name__ == "__main__":
	main();



