#coding=utf-8
"""归并排序 merge sort"""
def merge_sort(list = None):
    if list is None:
        return
    n = len(list)
    if n<=1:
        return list

    mid = int(n/2)
    left_list = merge_sort(list[:mid])
    right_list = merge_sort(list[mid:])
    """将两个有序的子序列 合并为一个新的整体"""
    # merge(left_list,right_list)
    left_poirt , right_poirt = 0, 0
    result = []
    while left_poirt < len(left_list) and right_poirt < len(right_list):
        if left_list[left_poirt] < right_list[right_poirt]:
            result .append(left_list[left_poirt])
            left_poirt += 1
        else:
            result .append(right_list[right_poirt])
            right_poirt += 1
    """无论左边的指针走到头 还是右边的列表走到头 都需要将列表内剩余的部分添加进result"""
    result += left_list[left_poirt:]
    result += right_list[right_poirt:]
    return  result

if __name__ == "__main__":
    list = [1,3,4,5,2,6,8,0,7]
    foo=merge_sort(list)
    print(foo)
