# Algorytm Bellmana-Forda O(VE)
# najksotrsze sciezki jesli wagi moga byc ujemne

# 1. inicjalizacja:
#    for v in V:
#        v.d = 9**9
#        v.parent = None
#    s.d = 0
# 2. relaksacje:
#    for v in range(|v| - 1):
#        for (u, v) in E:
#            Relax(u, v)
# 3. weryfikacja:
# czy dla kazdej krawedzi (u, v) in E:
#    v.d <= u.d + w(u, v)
# jezeli nasz warunek zawiedzie to ozancza ze mamy cykl o wadze ujemnej


A = [[(1, -1), (2, 4)], [(2, 3), (3, 2), (4, 2)],
     [()], [(1, 2), (2, 5)], [(3, -3)]]


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


def BellmanFord(A, s):
    n = len(A)
    tab_of_nodes = [Node(i, 9**9) for i in range(n)]
    tab_of_nodes[s].d = 0
    for index, elem in enumerate(A):
        for edge in elem:
            if edge != ():
                Relax(tab_of_nodes[index], tab_of_nodes[edge[0]], edge[1])
    for index, elem in enumerate(A):
        for edge in elem:
            if edge != ():
                if tab_of_nodes[index].d + edge[1] < tab_of_nodes[edge[0]].d:
                    print("Cykl o wadze ujemnej")
                    return 0

    for i in range(n):
        print("v1:", s, " v2:", i, " dist:", tab_of_nodes[i].d)
        while tab_of_nodes[i].parent != None:
            print(tab_of_nodes[i].value, '<-',
                  tab_of_nodes[i].parent.value, end=', ')
            i = tab_of_nodes[i].parent.value
        print("\n")


BellmanFord(A, 0)
