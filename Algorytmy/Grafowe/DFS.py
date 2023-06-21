# Algorytm DFS: listowa: O(V + E), macierzowa: O(V^2)
# G = (V, E), s in V

G = [(1, 3), (0, 2, 5), (1,), (0, 4), (3, 5), (1, 4)]


class Node():
    def __init__(self, val):
        self.value = val
        self.visited = False
        self.parent = None
        self.d = -1


def DFS_visit(G, s, time, tab_of_nodes):

    s.visited = True
    time[0] += 1
    s.t = time[0]
    for v in G[s.value]:
        if tab_of_nodes[v].visited == False:
            tab_of_nodes[v].parent = s
            DFS_visit(G, tab_of_nodes[v], time, tab_of_nodes)


def DFS(G):
    n = len(G)
    time = [0]
    tab_of_nodes = [Node(i) for i in range(n)]
    for node in tab_of_nodes:
        if node.visited == False:
            DFS_visit(G, node, time, tab_of_nodes)

    for i in range(n):
        print("v:", i + 1, " t:", tab_of_nodes[i].t)


DFS(G)
