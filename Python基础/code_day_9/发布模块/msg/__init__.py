#coding=utf-8
#该文件被导入时 先执行该文件
print("hahahhah")
#way1声明本包内，需要导入的py文件名称
#__all__ = ["sendmsg"];


#way2 声明需要导入的py文件名称（该写法兼容python 2和3） from 当前文件 import recmsg
from . import recmsg,sendmsg
