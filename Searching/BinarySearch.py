def Binary_Search(lst, target):


    """

    :param lst:
    :param target:
    Binary search is used to find the index of the target value
    Binary search time complexity  is constant O(n)
    """

    low,high = 0,len(lst)-1

    while low < high:

        mid = low + (high - low ) //2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return mid + 1
        else:
            high = mid - 1
    return -1


lst = [1,2,3,4,5,6,7,8,9,10]
target = 6
print(Binary_Search(lst, target))