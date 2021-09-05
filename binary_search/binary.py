#iterative
def binary_search(lst, target):
    left = 0
    right = len(lst) -1
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1
    return -1 

#recursive
def binarySearch(lst, left, right, target):
    mid = left + (right - left) // 2

    if left <= right:
        if lst[mid] == target:
            return mid 
        elif lst[mid] < target:
            return binarySearch(lst, mid+1, right, target)
        else:
            return binarySearch(lst, left, mid-1, target)
    else:
        return -1

lst = [1,2,3,4,5,6]
left = 0
right = len(lst) -1


print(binarySearch(lst,left,right,4))