from sys import stdin

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
    n = len(nm)
    mee = -1
    #node = nm[0]
    a = -1
    b = -1
    pris = 0
    for r in nm:
        a = r
        pris, b = minimum(a)
        if(mee<pris):
            mee == pris

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


    # SKRIV DIN KODE HER
def minimum(a):
    min = a[0]
    index = 0
    n = len(a)
    for i in range(1,n):
        if (a[i] != str and a[i]<min):
            min = a[i]
            index = i
    return min, index


nabomatrise = [["inf",5,3,7],
              [5,"inf","inf",1],
              [3,"inf","inf","inf"],
              [7,1,"inf","inf"]]

#for str in stdin:
#    linjer.append(str)
#n = len(linjer)
#nabomatrise = [None] * n
#node = 0
#for linje in linjer:
#   nabomatrise[node] = [Inf] * n
#    for k in linje.split():
#       data = k.split(':')
#        nabo = int(data[0])
#        vekt = int(data[1])
#        nabomatrise[node][nabo] = vekt
#    node += 1
#print nabomatrise
print mst(nabomatrise)
