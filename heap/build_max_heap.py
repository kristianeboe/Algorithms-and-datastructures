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

def build_max_heap(array):
    for i in range((len(array)/2)-1,-1,-1):
        max_heapify(array,i)

array = [4,1,3,2,16,9,10]
build_max_heap(array)
print array
