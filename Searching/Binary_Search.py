def binary_searching(arr, target):

    """
    Binary Search Algorithm time complexity:O(1)
    Binary Search works by comparing the target with the middle element.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

l = [17,18,19,20]
target = 19
print(binary_searching(l, target))



