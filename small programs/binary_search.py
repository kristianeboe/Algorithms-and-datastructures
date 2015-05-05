def binary_search(array, value):
    left = 0
    right = len(array)-1
    while left<=right:
        middle = (left+right)//2
        if array[middle] == value:
            break
        elif array[middle] > value:
            right = middle-1
        else:
            left = middle+1
    return middle


a = [1,2,3,4]
print binary_search(a,3)
