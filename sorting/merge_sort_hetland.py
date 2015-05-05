def merge_sort(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = merge_sort(lft)
    if len(rgt) > 1: rgt = merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

array = [2,5,1,3,7,4,6,9,8]
print merge_sort(array)

