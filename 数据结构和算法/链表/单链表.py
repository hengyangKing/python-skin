#coding=utf-8
class SingleLinkList(object):
    """单链表"""
    def __init__(self,note = None):
        self.__head = note

    def is_empty(self):
        return self.__head == None

    def length(self):
        """得到链表元素个数"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.nextAddr
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print (cur.item)
            cur = cur.nextAddr

    def add(self,item):
        """向链表头部添加元素"""
        node = Note(item)
        node.nextAddr = self.__head
        self.__head = node

    def append(self,item):
        """向链表尾部添加元素"""
        note = Note(item)
        if self.is_empty() :
            self.__head = note
        else:
            cur = self.__head
            while cur.nextAddr != None:
                cur = cur.nextAddr
            cur.nextAddr = note

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
        cur = self.__head
        prior = None
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.nextAddr
                else:
                    prior.nextAddr = cur.nextAddr
                break
            else:
                prior = cur
                cur = cur.nextAddr



    def search(self,item):
        """查找结点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.nextAddr
        return False



class Note(object):
    """节点类"""
    def __init__(self,item):
        self.item = item
        self.nextAddr = None

if __name__ == "__main__":
    list = SingleLinkList();
    if list.is_empty():
        list.append("1");
        list.append("2");
        list.append("3");
        list.append("4");
        list.append("5");

    list.add("100");
    list.insert("300",5);
    print (list.length());
    list.travel();
    print(list.search("400"))
    print("*"*90);
    list.remove("100");
    list.remove("300");
    list.travel();