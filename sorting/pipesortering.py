from sys import stdin
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

def sorter(A):
    randomized_quicksort(A,0,len(A)-1)
    return A

def finn(A, nedre, ovre):
    lower_bound = binary_search(A,nedre)
    upper_bound = binary_search(A,ovre)
    if A[lower_bound] > nedre and lower_bound != 0:
        lower_bound -= 1
    if A[upper_bound] < ovre and upper_bound != len(A)-1:
        upper_bound += 1
    return [A[lower_bound],A[upper_bound]]

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

liste = []
for x in stdin.readline().split():
    liste.append(int(x))

sortert = sorter(liste)

for linje in stdin:
    ord = linje.split()
    minst = int(ord[0])
    maks = int(ord[1])
    resultat = finn(sortert, minst, maks)
    print str(resultat[0]) + " " + str(resultat[1])
