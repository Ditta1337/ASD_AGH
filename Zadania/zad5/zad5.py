# Artur Dwornik

# Z listy krawedzi tworze liste sasiedztwa oraz tworze nowe krawedzie z kazdego do kazdego portalu o wadze 0.
# Wykonuję algorytm Dijkstry na nowym grafie i zwracam tablice z odleglosciami od wierzcholka a.
# Jezeli dlugosc wierzcholka a od b jest mniejsza niz nieskonczonosc, zwroc ja, w przeciwnym wypadku zwroc None.

# Zlozonosc obliczeniowa: O((E + S^2)log(V)), gdzie S to ilosc portali
# Zlozonosc pamieciowa: O(E + S^2)

from zad5testy import runtests
from queue import PriorityQueue


def relax(u, v, w, d):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        return 1
    return 0


def Dijkstra(G, a, n):
    d = [float("inf") for _ in range(n)]
    visited = [0 for _ in range(n)]
    q = PriorityQueue()

    d[a] = 0
    visited[a] = 1
    q.put([0, a])

    while not q.empty():
        _, u = q.get()
        visited[u] = 1
        for [v, w] in G[u]:
            if relax(u, v, w, d):
                if not visited[v]:
                    q.put([d[v], v])

    return d


def spacetravel(n, E, S, a, b):
    G = [[] for _ in range(n)]
    portals = []
    
    for portal in S: # O(S)
        portals.append([portal, 0])

    for edge in E:  # O(E)
        G[edge[0]].append([edge[1], edge[2]])
        G[edge[1]].append([edge[0], edge[2]])

    for counter, i in enumerate(S): # O(S^2)
        G[i].extend(portals[:counter])
        G[i].extend(portals[counter + 1:])


    d = Dijkstra(G, a, n)  # O((E + S^2)log(V))

    return d[b] if d[b] < float("inf") else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
