from random import randint

def partition(array, first, last):
    x = array[last]
    i = first-1
    for j in range(first,last):
        if array[j]<=x:
            i+=1
            old = array[i]
            array[i] = array[j]
            array[j] = old
    old = array[i+1]
    array[i+1] = array[last]
    array[last] = old

    return i+1

def randomized_partition(array,first,last):
    i = randint(first,last)
    old = array[last]
    array[last] = array[i]
    array[i] = old
    return partition(array,first,last)


def randomized_quicksort(array,first,last):
    if first < last:
        q = randomized_partition(array,first, last)
        randomized_quicksort(array,first,q-1)
        randomized_quicksort(array,q+1,last)

array = [2,8,7,1,3,5,6,4]
print array
randomized_quicksort(array,0,len(array)-1)
print array
