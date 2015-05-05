def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)
    return A

def heap_sort(array):
    build_max_heap(array)
    size = len(array)
    while size > 0:
        array[0], array[size - 1] = array[size - 1], array[0]
        max_heapify(array, 0)
        size -= 1
    return array

array = [9, 7, 6, 5, 3, 1, 4, 2, 8, 10]
build_max_heap(array)

print heap_sort(array)

