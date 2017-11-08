#coding=utf-8
class Stack(object):
    """栈的实现"""
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def push(self,item):
        """添加一个元素进入栈顶"""
        self.__items.append(item)

    def pop(self):
        """pop出栈顶元素"""
        self.__items.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__items:
            return self.__items[-1]
        else:
            return None

    def size(self):
        """元素个数"""
        return len(self.__items)


if __name__ == "__main__":
    stack = Stack()
    if stack.is_empty():
        stack.push("2")
    foo=stack.peek();
    print(foo);