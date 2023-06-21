# Artur Dwornik

# Za pomocą BFSa znajdujemy najkrotsza sciezke oraz jej dlugosc.
# Nastepnie po kolei z grafu usuwamy po krawedzi z najkrotszej sciezki
# i sprawdzamy BFSem czy najkrotsza odlegosc od s do t sie zwiekszyla.
# Jezeli tak, to zwracamy dana krawedz. Jezeli nigdy odleglosc sie nie
# zwiekszyla lub najkrotsza siezka z s do t nie istnieje, to zwracamy None.

# Zlozonosc obliczeniowa: O(E(V + E))
# Zlozonosc pamieciowa: O(E)

from zad4testy import runtests
#from collections import deque


def BFS(tab, n, s, t):
    q = [] # deque()
    visited = [0 for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]

    visited[s] = 1
    distance[s] = 0
    q.append(s)

    while q:
        u = q.pop(0) # q.popleft()
        for v in tab[u]:
            if not visited[v]:
                visited[v] = 1
                distance[v] = distance[u] + 1
                parent[v] = u
                q.append(v)
            if v == t:
                return parent, distance

    # Jezeli nigdy nie dotarlismy do t
    return parent, distance


def longer(G, s, t):
    n = 0

    for v in G:  # O(E)
        if v:
            n_tmp = max(v)
            n = max(n_tmp, n)

    n += 1

    parent, distance = BFS(G, n, s, t)  # O(V + E)

    if parent[t] == None:
        return None

    min_dist = distance[t]

    edges = []
    ind = t
    for _ in range(min_dist):  # O(E)
        edges.append([parent[ind], ind])
        ind = parent[ind]

    for edge in edges:  # O(E(V + E))
        G_cpy = [v for v in G]  # O(E)
        G_cpy[edge[0]].remove(edge[1])
        G_cpy[edge[1]].remove(edge[0])
        _, distance = BFS(G_cpy, n, s, t)

        # Przypadek distance[t] == -1: usunelismy most -> odlegosc inf
        if distance[t] > min_dist or distance[t] == -1:
            return edge

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
