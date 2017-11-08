#coding=utf-8
"""选择排序 select sort"""
def select_sort(list = None):
    if list is None:
        return
    n = len(list)
    for j in range(0,n-1):
        minIndex = j
        for i in range(j+1,n):
            if list[minIndex] > list[i]:
                minIndex = i
        list[j],list[minIndex] = list[minIndex],list[j]


if __name__ == "__main__":
    list = [1,3,4,5,2,6,8,0,7,9]
    select_sort(list)
    print(list)

