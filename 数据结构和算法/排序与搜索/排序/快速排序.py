#coding=utf-8
"""快速排序 quick sort"""

def quick_sort(list,first,last):
    if list is None:
        return
    if first >= last:
        return
    mid_value = list[first]
    """指向头尾的游标"""
    low = first
    high = last
    while low <high:
        """左移高位指针"""
        while low<high and list[high] >= mid_value:
            high -= 1
            """跳出循环发现满足 高低位指针重合或者高位指针指向数值<=mid_value 交换高低位指针数据"""
        list[low] = list[high]
        """右移地位指针"""
        while low<high and list[low]<mid_value:
            low += 1
        """同上"""
        list[high] = list[low]

    list[high] = mid_value

    quick_sort(list,first,low-1)
    quick_sort(list,low+1,last)

if __name__ == "__main__":
    list = [1,3,4,5,2,6,8,0,7]
    quick_sort(list,0,len(list)-1)
    print(list)


