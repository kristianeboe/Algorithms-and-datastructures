def max_heapify(array, index):
    l = 2*index+1
    r = 2*index+2
    if l<=len(array) and array[l] > array[index]:
        largest = l
    else:
        largest = index
    if r<=len(array) and array[r] > array[largest]:
        largest = r
    if largest != index:
        old = array[largest]
        array[largest] = array[index]
        array[index] = old
        max_heapify(array,largest)

array = [16,4,10,14,7,9,3,2,8]
print array
max_heapify(array,1)
print array
