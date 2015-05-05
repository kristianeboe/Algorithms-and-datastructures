from sys import stdin, stderr


class Graph():
    def __init__(self, M, probList):
        self.V = []
        self.E = []
        for r in range(0,len(M)):
            self.V.append(Vertex(r,probList[r]))

        for r in range(0,len(M)):
            for c in range(0,len(M[0])):
                if M[r][c]>0:
                    self.V[r].Adj.append(self.V[c])
                #self.E.append((self.V[r],self.V[c], M[r][c]))
                #self.E.append((self.V[c],self.V[r], M[c][r]))

class Vertex():
    def __init__(self,number,prob):
        self.number = number
        self.Adj = []
        self.prob = prob
        self.pi = None

def beste_sti(nm, sans):
    G = Graph(nm,sans)
    if G.V[0] == 0 or G.V[-1] == 0:
        return 0
    for v in G.V:
        print v.number, v.prob, v.Adj
    Q = G.V
    besteNode = Q[0]
    kumProb = -1
    que = []
    while Q:
        bestProb = kumProb
        for u in Q[besteNode.Adj]:
            #que.append(u)
            bestProb =
            if besteNode.prob*u.prob > :
                bestProb = besteNode.prob*u.prob
            Q.remove[0]


    return G.V
    # SKRIV DIN KODE HER

def extraxt_max():


n = int(stdin.readline())
sannsynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print beste_sti(nabomatrise, sannsynligheter)

