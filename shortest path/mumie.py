from sys import stdin, stderr

class GraphWeightInNode():
    def __init__(self, M, w):
        self.V = []
        for r in range(0,len(M)):
            self.V.append(VertexWithWeight(r,w[r]))
            for c in range(0,len(M[0])):
                #self.V[r].Adj[c] = M[r][c]
                if M[r][c] == 1:
                    self.V[r].Adj[c] = w[r]

class VertexWithWeight():
    def __init__(self,number,w):
        self.number = number
        self.w = w
        self.Adj = {}
        self.d = None
        self.pi = None

def initialize_single_source(G,s):
    for v in G.V:
        v.d = 1000
        v.pi = None
    s.d = 0

def relax(u,v):
    #print u.number, v.number
    if v.w < u.w*u.Adj[v.number]:
        v.d = u.w*u.Adj[v.number]
        v.pi = u
        #print v.number

def dijkstra(G,s):
    initialize_single_source(G,s)
    Q = list(G.V)
    u = s
    return_list = []
    while Q:
        u = extract_min_path(Q,u)
        Q.remove(u)
        return_list.append(u.number)
        if u.w == 0:
            return 0
        if u.number == len(G.V)-1:
            break
        for v in u.Adj.iterkeys():
            v  = G.V[v]
          #  print v.number
            relax(u,v)
    return return_list


    #return_list.append(G.V[-1].number)
    #G.V[-1].pi = u
    #print G.V[return_list[0]].number
    #print G.V[return_list[0]].pi
    #while G.V[return_list[0]].pi.number.a != 0:
    #    print G.V[return_list[0]].pi.number
    #    return_list.insert(0,G.V[return_list[0]].pi.number)
    #    print return_list[0]
    #return return_list.reverse()

def extract_min_path(u):
    min_ = None
    r = None
    for v in u.Adj:
        if

def extract_min_path(Q,u):
    min_ = None
    r = None
    for v in Q:
        #print u.Adj
        if (v.w > min_ and v.number in u.Adj) or min_ == None:
            min_ = v.w
            r = v
    return r

def beste_sti(nm, sans):
    G = GraphWeightInNode(nm,sans)
    for v in G.V:


    path = dijkstra(g,g.V[0])
    if path == 0:
        return 0
    path_str = ""
    for i in path:
        path_str+=str(i)+"-"
    path_str = path_str[0:len(path_str)-1]
    return path_str

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
