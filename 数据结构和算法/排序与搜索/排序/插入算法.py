#coding=utf-8
"""插入排序 insert sort"""
def insert_sort(list = None):
    if list is None:
        return
    n = len(list)
    """外层循环表示每次从无序列表中取出多少个元素这样的过程"""
    for j in range(1,n):
        """i 表示 内层循环起始位置"""
        """内层循环表示 执行从右边无序列表取出第一个元素 即i位置的元素，将其插入到前面正确的位置中"""
        i = j
        while i>0:
            if list[i]<list[i-1]:
                list[i],list[i-1] = list[i-1],list[i]
                i -= 1
            else:
                break

if __name__ == "__main__":
    list = [1,3,4,5,2,6,8,0,7,9]
    insert_sort(list)
    print(list)