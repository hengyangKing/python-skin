#coding=utf-8
"""single_cycle_link list"""
class SingleCycleLinkList(object):
    """单链表循环链表"""
    def __init__(self,note = None):
        self.__head = note
        """最后一项addr 指向 __head """
        if note:
            note.nextAddr = note

    def is_empty(self):
        return self.__head == None

    def length(self):
        """得到链表元素个数"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.nextAddr != self.__head:
            count += 1
            cur = cur.nextAddr
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.nextAddr != self.__head:
            print (cur.item)
            cur = cur.nextAddr
        """退出循环 cur 指向尾结点 但是尾结点元素未打印"""
        print(cur.item)


    def add(self,item):
        """向链表头部添加元素"""
        node = Note(item)
        if self.is_empty():
            self.__head = node
            node.nextAddr = node
            return
        cur = self.__head
        while cur.nextAddr != self.__head:
            cur = cur.nextAddr
        """退出循环 cur 指向尾结点 """
        node.nextAddr = self.__head
        self.__head = node
        cur.nextAddr = self.__head

    def append(self,item):
        """向链表尾部添加元素"""
        note = Note(item)
        if self.is_empty() :
            self.__head = note
            note.nextAddr = note
        else:
            cur = self.__head
            while cur.nextAddr != self.__head:
                cur = cur.nextAddr
            cur.nextAddr = note
            note.nextAddr = self.__head

    def insert(self,item,index):
        """向某一个位置插入元素"""
        if index <= 0 :
            self.add(item)
        elif index > self.length()-1:
            self.append(item)
        else:
            prior = self.__head
            count = 0
            while count < (index-1):
                prior = prior.nextAddr
                count += 1
            """循环退出后 prior 指向 index-1位置"""
            note = Note(item)
            note.nextAddr = prior.nextAddr
            prior.nextAddr = note

    def remove(self,item):
        """删除某个元素"""
        if self.is_empty():
            return
        cur = self.__head
        prior = None
        while cur.nextAddr != self.__head:
            if cur.item == item:
                """先判断是否为头结点"""
                if cur == self.__head:
                    """头结点"""
                    """修改尾结点"""
                    rear = self.__head
                    while rear.nextAddr != self.__head:
                        rear = rear.nextAddr
                    self.__head = cur.nextAddr
                    rear.nextAddr = self.__head

                else:
                    """中间结点"""
                    prior.nextAddr = cur.nextAddr
                return
            else:
                prior = cur
                cur = cur.nextAddr
        """尾结点"""
        if cur.item == item:
            if cur == self.__head:
                """链表只有一个结点"""
                self.__head = None
            else:
                prior.nextAddr = cur.nextAddr



    def search(self,item):
        """查找结点是否存在"""
        if self.is_empty():
            return False

        cur = self.__head
        while cur.nextAddr != self.__head:
            if cur.item == item:
                return True
            else:
                cur = cur.nextAddr
        if cur.item == item:
            return True

        return False



class Note(object):
    """节点类"""
    def __init__(self,item):
        self.item = item
        self.nextAddr = None