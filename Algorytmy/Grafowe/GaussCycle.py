# Gauss Cycle, O(V+E)

class Node():
    def __init__(self):
        self.visited = False
        self.edges = []

G = [(1, 2), (0, 2, 3, 5), (0, 1, 3, 5), (1, 2, 4, 5), (3, 5), (1, 2, 3, 4)] #(7 ,8), (6, 9), (6, 9), (7, 8)

def DFSGauss(G, index, tab_of_nodes, ret):
    tab_of_nodes[index].visited = True
    for v in G[index]:
        if v not in tab_of_nodes[index].edges:
            tab_of_nodes[index].edges.append(v)
            tab_of_nodes[v].edges.append(index)
            DFSGauss(G, v, tab_of_nodes, ret)
    ret.append(index)
    
def areNodesEven(G):
    for elem in G:
        if type(elem) == int or len(elem) % 2 != 0:
            return False
    return True

def DFSGaussCycle(G):
    n = len(G)
    ret = []
    tab_of_nodes = [Node() for _ in range(n)]
    flag = 0
    if areNodesEven(G):
        for index in range(n):
            if not tab_of_nodes[index].visited:
                flag += 1
                DFSGauss(G, index, tab_of_nodes, ret)
        if flag != 1:
            print("Cykl nie jest spojny")
        else:
            ret = ret[::-1]
            print(ret)
    else:
        print("Jakis wierzcholek nie ma stopnia patrzystego")

DFSGaussCycle(G)