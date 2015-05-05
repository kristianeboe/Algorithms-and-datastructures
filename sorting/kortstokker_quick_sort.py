from sys import stdin
from itertools import repeat
from random import randint


def partition(array, first, last):
    x = array[last][0]
    i = first-1
    for j in range(first,last):
        if array[j][0]<=x:
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

def merge(decks):
    randomized_quicksort(decks,0,len(decks)-1)
    word = ""
    for t in decks:
        word += t[1]
    return word
    # SKRIV DIN KODE HER

decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.extend(deck)
print merge(decks)
