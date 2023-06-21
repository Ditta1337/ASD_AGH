# Algorytm Prima
# znajdowanie minimalnego drzewa rozpinajacego
# do spojnej czesci drzewa rozpinajacego dodajemy kolejne krawedzie
# o najmniejszej wadze ktroe rozszerzaja drzewo

# 1. startujemy z wierzcholka s
# 2. wszystkie wierzcholki umieszczamy w kolejce priorytetowej
#    z waga inf (nie robimy tego)
# 3. zamieniamy wage wierzcholka s na 0
# 4. poki sa wierzcholki w kolejce priorytetowej:
#   - wyjmij wierzcholek t o minimalnej wadze
#   - dla kazdej krawedzi {t, u}, jesli waga u >= w(t, u), to
#     zamien wage u na w(t, u) i uaktualnij parenta u oraz pole visited

from queue import PriorityQueue

A = [[0, 2, 0, 6, 0],
     [2, 0, 3, 8, 5],
     [0, 3, 0, 0, 7],
     [6, 8, 0, 0, 9],
     [0, 5, 7, 9, 0]]

class Node():
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.parent = None
        self.visited = False

def Prim(A, s):
    n = len(A)
    tab_of_nodes = [Node(i, 9**9) for i in range(n)]
    tab_of_nodes[s].weight = 0
    tab_of_nodes[s].visited = True
    q = PriorityQueue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in range(n):
            if A[u][v] > 0 and tab_of_nodes[v].visited == False:
                if A[u][v] < tab_of_nodes[v].weight:
                    tab_of_nodes[v].weight = A[u][v]
                    tab_of_nodes[v].parent = u
                if tab_of_nodes[v].visited == False:
                    q.put(v)
                    tab_of_nodes[v].visited = True

    for i in range(n):
        if tab_of_nodes[i].parent != None:
            print("v1:", tab_of_nodes[i].value, " v2:", tab_of_nodes[i].parent,
                  " w:", A[tab_of_nodes[i].value][tab_of_nodes[i].parent])


Prim(A, 0)
