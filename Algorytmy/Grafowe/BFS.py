# Algorytm BFS: listowa: O(V + E), macierzowa: O(V^2)
# G = (V, E), s in V

from collections import deque

class Node():
    def __init__(self):
        self.d = -1
        self.parent = None
        self.visited = False

G = [(1, 3), (0, 2, 5), (1, 2), (0, 3, 4), (0, 4), (1, 4)]

def BFS(G, s):
    Q = deque()
    tab_of_nodes = [Node() for _ in range(len(G))]

    tab_of_nodes[s].visited = True
    tab_of_nodes[s].d = 0
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if tab_of_nodes[v].visited == False:
                tab_of_nodes[v].visited = True
                tab_of_nodes[v].d = tab_of_nodes[u].d + 1
                tab_of_nodes[v].parent = u
                Q.append(v)

    for i in range(len(tab_of_nodes)):
        print("v:", i + 1, " d:", tab_of_nodes[i].d)
    
BFS(G, 0)