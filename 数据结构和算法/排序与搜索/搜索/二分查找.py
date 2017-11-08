#coding=utf-8
"""二分查找 binary search"""
def binary_search_recursion(list = None,item = None):
    """递归"""
    if list is None or item is None:
        return False
    n = len(list)
    if n > 0 :
        """找到中间位置"""
        mid_index = int((int(0 + n))/2)

        if list[mid_index] == item:
            return True
        elif item <list[mid_index]:
            return binary_search_recursion(list[:mid_index],item)
        else:
            return binary_search_recursion(list[mid_index+1:],item)

    return False


def binary_search(list = None,item = None):
    if list is None or item is None:
        return
    n = len(list)
    first = 0
    last = n-1
    while first <= last:
        mid_index = int((first+last)/2)
        if list[mid_index] == item:
            return True
        elif item < list[mid_index]:
            last = mid_index -1
        else:
            first = mid_index +1

    return False

if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9,10]
    foo = binary_search_recursion(list,50)
    print(foo)

    foo = binary_search_recursion(list,5)
    print(foo)

    foo = binary_search(list,50)
    print(foo)

    foo = binary_search(list,5)