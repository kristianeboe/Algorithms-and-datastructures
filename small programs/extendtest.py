from itertools import repeat


l1 = "i:1,3,5,8"
l2 = "n:2"
l3 = "t:4,7"
l4 = "a:6"
l5 = "v:9"

def merge(decks):
    mid = len(decks)//2
    lft, rgt = decks[:mid], decks[mid:]
    if len(lft) > 1: lft = merge(lft)
    if len(rgt) > 1: rgt = merge(rgt)
    res = []
    while lft and rgt:
        if lft[-1][0] >= rgt[-1][0]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    sorted_list = (lft or rgt) + res
    return sorted_list

decks = []

index, list = l1.split(':')
print list

#for line in stdin:
(index, list) = l1.split(':')
deck = zip(map(int, list.split(',')), repeat(index))
decks.extend(deck)

(index, list) = l2.split(':')
deck = zip(map(int, list.split(',')), repeat(index))
decks.extend(deck)

(index, list) = l3.split(':')
deck = zip(map(int, list.split(',')), repeat(index))
decks.extend(deck)

(index, list) = l4.split(':')
deck = zip(map(int, list.split(',')), repeat(index))
decks.extend(deck)

(index, list) = l5.split(':')
deck = zip(map(int, list.split(',')), repeat(index))
decks.extend(deck)

print merge(decks)
