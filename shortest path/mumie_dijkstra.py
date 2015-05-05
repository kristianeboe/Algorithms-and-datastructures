from sys import stdin, stderr

class Graph():
    def __init__(self, M,probList):
        self.V = []
#        self.E = []
        for r in range(0,len(M)):
            self.V.append(Vertex(r,probList[r]))
        for r in range(0,len(M)):
            for c in range(0,len(M[0])):
                if M[r][c] < 1000 and M[r][c] != 0:
                    self.V[r].Adj[c] = self.V[c].prob
             #   self.V[r].append(c)
#                self.E[(V[r],V[c])] = M[r][c]
 #               self.E[(V[c],V[r])] = M[c][r]

class Vertex():
    def __init__(self,number,prob):
        self.number = number
        self.Adj = {}
        self.prob = prob
        self.pi = None


def initialize_single_source(G,s):
    for v in G.V:
        v.prob = 0
        v.pi = None
    G.V[0].prob = s

def relax(u,v):
   # print v.prob, u.prob*u.Adj[v.number]
    #if v.number in u.Adj and v.prob < u.prob*u.Adj[v.number]:

    if v.prob < u.prob*u.Adj[v.number]:
        v.prob = u.prob*u.Adj[v.number]
        v.pi = u

def dijkstra(G,s):
    initialize_single_source(G,s)
    Q = list(G.V)
    #path = []
    while Q:
        u = extract_max_prob(Q)
        Q.remove(u)
    #    path.append(u.number)
        for v in u.Adj.iterkeys():
            v  = G.V[v]
            relax(u,v)
    #return path

def extract_max_prob(Q):
    max_ = None
    node = None
    for v in Q:
        #print "v in Q: " + str(v.number)
     #   print v.number, v.prob
        if v.prob > max_ or max_ == None:
            max_ = v.prob
            node = v
    return node


def beste_sti(nm, sans):
    G = Graph(nm,sans)
    s = G.V[0].prob
    dijkstra(G,s)
    target = G.V[-1]
    seq = [target.number]
    while seq[-1] != 0:
        node = target.pi.number
        seq.append(node)
        target = G.V[node]
    seq.reverse()
    if seq == 0:
        return 0
    path = ""
    for a in seq:
        if G.V[a].prob == 0:
            return 0
        path += str(a)+"-"
    path = path[0:len(path)-1]
    return path

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
