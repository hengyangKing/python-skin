#coding=utf-8
"""希尔排序 shell sort"""
"""希尔排序整体而言是插入排序的改进版"""

def shell_sort(list = None):
    if list is None:
        return
    n = len(list)
    """gap 将数列从中间分开 本质还是插入算法"""
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap,n):
            """j 为内层循环的起始值 gap gap+1 gap+2 。。。。n"""
            j = i
            while j > 0:
                if list[j]<list[j-gap]:
                    list[j],list[j-gap] = list[j-gap],list[j]
                    j -= gap
                else:
                    break
        gap = int(gap / 2)


if __name__ == "__main__":
    # list = [1,3,4,5,2,6,8,0,7]
    list = [2,1]
    shell_sort(list)
    print(list)