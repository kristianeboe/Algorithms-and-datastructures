from sys import stdin
from itertools import repeat

def merge(comb):
    word = ""
    for key, val in comb.iteritems():
        word += comb[key]
    return word

comb = {}
for line in stdin:
    index, list = line.split(':')
    list = [int(x) for x in list.split(',')]
    for a in list:
        comb[a] = index


print merge(comb)
