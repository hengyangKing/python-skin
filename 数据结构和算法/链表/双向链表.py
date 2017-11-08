#coding=utf-8
"""double link list"""
class Note(object):
    def __init__(self,item):
        self.item = item
        self.nextAddr = None
        self.priorAddr = None

class DoubelLinkList(object):
    def __init__(self,note = None):
        self.__head = note

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None :
            count += 1
            cur = cur.nextAddr
        return count
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur)
            cur = cur.nextAddr

    def add(self,item):
        """添加进头部"""
        note = Note(item)
        note.nextAddr = self.__head
        self.__head = note
        note.nextAddr.priorAddr = note

    def append(self,item):
        """添加进尾部"""
        note = Note(item)
        if self.is_empty():
            self.__head = note
        else:
            cur = self.__head
            while cur.nextAddr != None:
                cur = cur.nextAddr
            cur.nextAddr = note
            note.priorAddr =cur

    def insert(self,item,index):
        if index <= 0:
            self.add(item)
        elif index > (self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < index:
                count += 1
                cur = cur.nextAddr
            note = Note(item)
            note.nextAddr = cur
            note.priorAddr = cur.priorAddr
            cur.priorAddr.next = note
            cur.priorAddr = note

    def remove(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.nextAddr
                    if cur.nextAddr:
                        """判断链表只有一个结点"""
                        cur.nextAddr.priorAddr = None
                else:
                    cur.priorAddr.next = cur.nextAddr
                    if cur.nextAddr:
                        cur.nextAddr.priorAddr = cur.priorAddr
                break
            else:
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

if __name__ == "__main__":
    list = DoubelLinkList();
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