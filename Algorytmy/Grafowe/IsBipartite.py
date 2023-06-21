
class Node():
    def __init__(self):
        self.visited = False
        self.color = 0

#G = [[4, 5], [4], [6, 7], [4, 5], [0, 1, 3], [3, 6], [2], [0]]
G = [[1, 4], [0, 2], [1, 3], [2, 4], [3, 0]]

def DFS(G, i, tab_of_nodes):
    tab_of_nodes[i].visited = True
    for v in G[i]:
        if tab_of_nodes[v].visited == False:
            tab_of_nodes[v].color = not tab_of_nodes[i].color
            DFS(G, v, tab_of_nodes)
        elif tab_of_nodes[v].color == tab_of_nodes[i].color:
            return 1


def DFSBipartite(G):
    flag = 0
    tab_of_nodes = [Node() for _ in range(len(G))]
    tab_of_nodes[0].color = 1
    #tab_of_nodes[0].color = 0
    for i in range(len(G)):
        if tab_of_nodes[i].visited == False:
            flag = DFS(G, i, tab_of_nodes)
            if flag == 1:
                break
    if flag:
        print("Nie jest grafem bipartitym")
    else:   
        print("Jest grafem bipartitym")

DFSBipartite(G)