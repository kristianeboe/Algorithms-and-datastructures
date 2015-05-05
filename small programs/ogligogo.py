from sys import stdin

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
    n = len(nm)
    mst = [0]
    paths = []
    mee = -1
    for r in range(0,n):
        for c in range(0,n):
            paths += [[nm[r][c],c]]
        min = Inf
        for i in paths:
            if i[0]<min and i[1] not in mst:
                min = i[0]
                temp = i[1]
        if min != Inf and min > mee:
            mee = min
        mst.append(temp)
        for v in paths:
            if v[1] in mst:
                paths.remove(v)
#        print paths
#        print mst
#        print min
        if len(mst) == n:
            return mee
    return mee


linjer = []
for str in stdin:
    linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * n
    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
    node += 1

nm = [[Inf,5,3,7,],
      [5,Inf,Inf,1],
      [3,Inf,Inf,Inf],
      [7,1,Inf,Inf]]
print mst(nabomatrise)
