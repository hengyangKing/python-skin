#coding=utf-8
class Queue(object):
    """队列的实现"""
    def __init__(self):
        self.__list = []

    def is_empty(self):
        """是否是空队列"""
        return len(self.__list)
    def en_queue(self,item):
        """入队列"""
        self.__list.append(item)

    def de_queue(self):
        """出队列"""
        return self.__list.pop(0)

    def size(self):
        return len(self.__list)

if __name__=="__main__":
    q = Queue()
    for i in range(0,4):
        q.en_queue(i)

    for i in range(q.size()):
        print(q.de_queue());
