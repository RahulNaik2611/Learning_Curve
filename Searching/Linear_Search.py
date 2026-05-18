def linearSearch(lst, target):

    """
    linear search is basical used for searching through the list
    time complexity: O(n)
    linear search basically used for UnSorted list and sorted list
    """

    i = 0

    while i < len(lst):

        if lst[i] == target:
            return i     # it's return the index value
        i += 1
    return -1


list = [5,3,8,2,6,1]
target = 2
print(linearSearch(list, target))


