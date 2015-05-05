from sys import stdin, maxint

def korteste_rute(rekkefolge, nabomatrise, byer):
    sum_ = 0
    if len(rekkefolge) == 0:
        return "umulig"

    for by in range(1,len(rekkefolge)):
        from_ = rekkefolge[by-1]
        to_ = rekkefolge[by]
        price = nabomatrise[from_][to_]
        if price >= maxint/3:
            return "umulig"
        sum_ += price
        from_ = to_
        to_ = rekkefolge[by]
    return sum_


def Floyd_Warshall(W):
    n = len(W)
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                W[i][j] = min(W[i][j],W[i][k]+W[k][j])
    return W


testcases = int(stdin.readline())
for test in range(testcases):
    byer = int(stdin.readline())
    rekkefolge = [int(by) for by in stdin.readline().split()]
    rekkefolge.append(rekkefolge[0])
    nabomatrise = []
    for by in range(byer):
        naboer = []
        for distanse in stdin.readline().split():
            distanse = int(distanse)
            if distanse == -1:
                distanse = maxint/3
            naboer.append(distanse)
        nabomatrise.append(naboer)
    nabomatrise = Floyd_Warshall(nabomatrise)
    print korteste_rute(rekkefolge, nabomatrise, byer)


