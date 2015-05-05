from sys import stdin
from itertools import repeat

def merge(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]

    if len(lft) > 2: lft = merge(lft)
    if len(rgt) > 2: rgt = merge(rgt)
    print lft
    print rgt
    res = []
    while lft and rgt:
        if (lft[-1][0] >= rgt[-1][0]):
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    sortedL = (lft or rgt) + res
    print "sortedL: "+ str(sortedL)
    word = ""
    for t in sortedL:
        word += t[1]
    return word

decks = [(1,'i'),(3,'i'),(5,'i'),(8,'i'), (2,'n'), (4,'t'),(7,'t'), (6,'a'), (9,'v')]

#for line in stdin:
#    (index, list) = line.split(':')
#   deck = zip(map(int, list.split(',')), repeat(index))
#   decks.extend(deck)

print merge(decks)
