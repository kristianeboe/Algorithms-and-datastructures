from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    rot = Node()
    for o, pos in ordliste:
        node = rot
        for n in range(len(o)):
            if o[n] not in node.barn:
                node.barn[o[n]] = Node()
                node = node.barn[o[n]]
                #print(o[n])
                #node.posi.apend(pos)
            else:
                node = node.barn[o[n]]
                #node.posi.apend(pos)
        node.posi.append(pos)

    return rot


def posisjoner(ord, indeks, toppnode):
    node = toppnode
    for i in range(indeks, len(ord)):
        if ord[i] in node.barn:
            node = node.barn[ord[i]]
        return node.posi


try:
    setning = "ha ha mons har en hund med moms hun er en hunn"
    ord = setning.split()
    # ord = ["ha","ha","mons","har","en","hund","med","moms"]
    sord= ["ha","mons"]
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in sord:
        print("a")
        sokeord = sokeord.strip()
        print(sokeord + ":"),
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print(p)
except:
    traceback.print_exc(file=stderr)
