def max_heapify(array, index):
    l = 2*index+1
    r = 2*index+2
    if l<len(array) and array[l] > array[index]:
        largest = l
    else:
        largest = index
    if r<len(array) and array[r] > array[largest]:
        largest = r
    if largest != index:
        old = array[largest]
        array[largest] = array[index]
        array[index] = old
        max_heapify(array,largest)
    return array

def build_max_heap(array):
    for i in range((len(array)/2)-1,-1,-1):
        max_heapify(array,i)

def heapsort1(array):
#    build_max_heap(array)
    sorted_array = []
    for i in range(len(array)-1,-1,-1):
        old = array[0]
        array[0] = array[i]
        array[i] = old
        sorted_array.insert(0,array.pop())
        max_heapify(array,0)
    return sorted_array

def heapsort2(array):
    print max_heapify(array,1)

    #while array:

array = [9, 7, 6, 5, 3, 1, 4, 2, 8, 10]
heapsort2(array)
