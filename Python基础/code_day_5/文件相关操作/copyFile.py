#coding=utf-8

fileName = raw_input("请输入需要赋值的文件名");

index=fileName.rfind(".");
new_fileName = fileName[0:index]+"(复件)"+fileName[index:];
file_obj = open(fileName, "r");
newFile_obj = open(new_fileName,"w");
newFile_obj.write(file_obj.read());

file_obj.close();
newFile_obj.close();

print("success");

