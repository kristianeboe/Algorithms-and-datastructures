from sys import stdin, stderr

def beste_sti(nm, sans):
    # START IKKE-UTDELT KODE
    n = len(sans)
    ferdig = [False] * n
    ksans = [0.0] * n # kummulativ sannsynlighet
    ksans[0] = sans[0]
    beste_node = 0
    path = []
    for i in range(n):
        node = beste_node
        path.append(beste_node)
        if beste_node == n-1:
            break
        ferdig[node] = True
        hoyeste_ksans = -1.0
        for nabo in range(n):
            if not ferdig[nabo]:
                if nm[node][nabo]:
                    tilbud = ksans[node] * sans[nabo]
                    if tilbud > ksans[nabo]:
                        ksans[nabo] = tilbud
                if ksans[nabo] > hoyeste_ksans:
                    beste_node = nabo
                    hoyeste_ksans = ksans[nabo]
    # returner beste kummulative sannsynlighet for aa komme seg
    # til den siste noden
    path_str = ""
    for i in path:
        path_str+=str(i)+"-"
    path_str = path_str[0:len(path_str)-1]
    return path_str

    # SLUTT IKKE-UTDELT KODE





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
