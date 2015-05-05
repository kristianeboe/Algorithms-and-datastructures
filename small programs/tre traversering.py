from sys import stdin

class Node:
    barn = None
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0
        self.visited = False
        self.finished = False

def dfs(rot):
    stack = [rot]
    while len(stack) > 0:
        node = stack[len(stack)-1]
        if node.ratatosk:
            return len(stack)-1
        if node.nesteBarn == len(node.barn):
            stack.pop()
        else:
            stack.append(node.barn[node.nesteBarn])
            node.nesteBarn += 1

def bfs(rot):

    # SKRIV DIN KODE HER

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    # SKRIV DIN KODE HER
