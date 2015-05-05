class Graph():
    def __init__(self, M):
        self.V = []
        self.E = []
        for r in range(0,len(M)):
            self.V.append(Vertex(r))
            for c in range(0,len(M[0])):
                self.V[r].append(c)
                self.E[(V[r],V[c])] = M[r][c]
                self.E[(V[c],V[r])] = M[c][r]

            #    self.V[r].Adj[c] = M[r][c]
            #    if M[r][c] < 1000 and M[r][c] != 0:

class GraphWeightInNode():
    def __init__(self, M, w):
        self.V = []
        for r in range(0,len(M)):
            self.V.append(Vertex(r,w[r]))
            for c in range(0,len(M[0])):
                self.V[r].Adj[c] = M[r][c]
                #self.E[(r,c)] = M[r][c]



class Vertex():
    def __init__(self,number):
        self.number = number
        self.Adj = []
        self.d = None
        self.pi = None

class VertexWithWeight():
    def __init__(self,number,w):
        self.number = number
        self.w = w
        self.Adj = {}
        self.d = None
        self.pi = None

def relax(u,v):
    if v.d > u.d+u.Adj[v.number]:
        v.d = u.d+u.Adj[v.number]
        v.pi = u

def initialize_single_source(G,s):
    for v in G.V:
        v.d = 1000
        #bytt til sys.float_info.max
        v.pi = None
    s.d = 0

M = [[0,1,3],
     [10000,0,1],
     [10000,10000,0]]
