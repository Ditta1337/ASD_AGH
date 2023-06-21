from collections import deque

G = [[1], [5], [0], [1, 4], [2], [6], [3]]

class Node():
    def __init__(self):
        self.d = -1
        self.parent = None
        self.visited = False

def BFSFindCycles(G, s):
    Q = deque()
    tab_of_nodes = [Node() for _ in range(len(G))]


    tab_of_nodes[s].visited = True
    tab_of_nodes[s].d = 0
    Q.append(s)
    cycle = 0
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if tab_of_nodes[v].visited == False:
                tab_of_nodes[v].visited = True
                tab_of_nodes[v].d = tab_of_nodes[u].d + 1
                tab_of_nodes[v].parent = u
                Q.append(v)
            elif tab_of_nodes[u].parent != tab_of_nodes[v]:
                cycle += 1

    
    print("Cycles detected:", cycle)

BFSFindCycles(G, 0)