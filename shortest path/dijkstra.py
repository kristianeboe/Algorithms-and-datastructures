class Graph():
    def __init__(self, M):
        self.V = []
        self.E = []
        for r in range(0,len(M)):
            self.V.append(Vertex(r))
            for c in range(0,len(M[0])):
                if M[r][c] < 1000 and M[r][c] != 0:
                    self.V[r].Adj[c] = M[r][c]
             #   self.V[r].append(c)
#                self.E[(V[r],V[c])] = M[r][c]
 #               self.E[(V[c],V[r])] = M[c][r]
        for v in self.V:
            print v.Adj

class Vertex():
    def __init__(self,number):
        self.number = number
        self.Adj = {}
        self.d = None
        self.pi = None


def initialize_single_source(G,s):
    for v in G.V:
        v.d = 1000
        v.pi = None
        print v.number, v.d
    s.d = 0

def relax(u,v):
    if v.d > u.d+u.Adj[v.number]:
        v.d = u.d+u.Adj[v.number]
        v.pi = u

def dijkstra(G,s):
    initialize_single_source(G,s)
    Q = list(G.V)
    while Q:
        u = extract_min(Q)
        Q.remove(u)
        for v in u.Adj.iterkeys():
            v  = G.V[v]
            relax(u,v)

def extract_min(Q):
    min_ = None
    r = None
    for v in Q:
        if v.d < min_ or min_ == None:
            min_ = v.d
            r = v
    return r



M = [[0,1,3],
     [10000,0,1],
     [10000,10000,0]]

W = [[0,3,1000,1000,1000,1000,1000],
    [1000,0,4,9,1000,5,1000],
    [1000,1000,0,4,5,1000,1000],
    [3,1000,1000,0,1000,1000,1],
    [1000,1000,1000,5,0,1000,4],
    [4,1000,1000,1000,1,0,1000],
    [1000,1000,1000,1000,1000,2,0]]

g = Graph(W)

dijkstra(g,g.V[0])

for i in g.V:
    print i.d
