def dijkstra(G, s):
    Q,S = [(0,s)], set()

    while Q:
        d,u = heappop(Q)
        if u in S: continue
        S.add(u)
        yield u, d
        for v in G[u]:
            heappush(Q,(d+G[u][v],v))
