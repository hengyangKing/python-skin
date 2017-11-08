#coding=utf-8
"""冒泡排序 bubble sort"""

def bubble_sort(list = None):
    if list is None:
        return
    n = len(list)
    for i in range(n-1):
        """添加count 优化最优情况排序时间"""
        count = 0
        for j in range(0,n-i-1):
          """0--->(n-1)"""
          if list[j]>list[j+1]:
              list[j],list[j+1] = list[j+1],list[j]
        if 0 == count:
            return

if __name__ == "__main__":
    list = [1,3,4,5,2,6,8,0,7,9]
    bubble_sort(list)
    print(list)
