# Algorytm Dijkstry, O(ElogV)
# algorytm elementarny, ale w kazdym
# kroku skacze do prawdziwego wierzcholka
# Uwaga: wagi nie musza byc naturalne, ale musza byc nieujemne
# Notacja: G = (V, E), w: E -> R+ wejsciowy graf wazony
# w(u, v) = waga krawedzi {u, v}
# u.d = oszacowana odleglosc od wierzcholka s
# u.parent = poprzednik na najkrotszej scieze (ze startowego do u)

# 1. startujemy z wierzcholka s
# 3. zamieniamy oszacowana odleglosc wierzcholka s na 0
# 4. poki sa wierzcholki w kolejce priorytetowej:
#   - wyjmij wierzcholek u o minimalnej wartosci u.d
#   - dla kazdej krawedzi {u, v} wykonaj relaksacje:
#           def Relax(u,v,w): w(u, v)
#               if u.d + w < v.d:
#                   v.d = u.d + w
#                   v.parent = u

from queue import PriorityQueue
A = [[(1, 3), (2, 4)], [(2, 3), (3, 2), (4, 2)], [], [(4, 8)], [(2, 7)]]


class Node():
    def __init__(self, value, d):
        self.value = value
        self.d = d
        self.parent = None
        self.visited = False


def Relax(u, v, w):
    if u.d + w < v.d:
        v.d = u.d + w
        v.parent = u


def Dijkstra(A, s):
    n = len(A)
    tab_of_nodes = [Node(i, 9**9) for i in range(n)]
    tab_of_nodes[s].d = 0
    q = PriorityQueue()
    q.put(s, 0)
    while not q.empty():
        u = q.get()
        for elem in A[u]:
            Relax(tab_of_nodes[u], tab_of_nodes[elem[0]], elem[1])
            if tab_of_nodes[elem[0]].visited == False:
                q.put(elem[0], tab_of_nodes[elem[0]].d)
                tab_of_nodes[elem[0]].visited = True
    
    for i in range(n):
        print("v1:", s, " v2:", i, " dist:", tab_of_nodes[i].d)
        while tab_of_nodes[i].parent != None:
            print(tab_of_nodes[i].value, '<-', tab_of_nodes[i].parent.value, end=', ')
            i = tab_of_nodes[i].parent.value
        print("\n")


Dijkstra(A, 0)


