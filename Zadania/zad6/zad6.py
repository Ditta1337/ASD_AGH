# Artur Dwornik

# Z danej listy tworzę nową reprezentację listową grafu dodając zrodlo i ujscie (s oraz t).
# Ze zrodla wyprowadzam krawedzie do pracownikow (o przepusotowosci 1), a z prac porawdze
# krawedzie do ujscia (o przepustowosci 1). Nastepnie co iteracje algorytmu Edmondsa-Karpa,
# szukam sciezek powiekszajacych w grafie za pomoca BFS'a. Jezeli takowa sciezka jest
# znaleziona, do koncowego wyniku dodaje 1 oraz tworze z niej krawedzie wsteczne, uzywajac 
# naszego grafu rowniez jako sieci residualnej. Algorutm konczy dzialanie jak BFS nie moze 
# znalezc juz zadnej sciezki powiekszajacej.

# Zlozonosc obliczeniowa: O(VE), gdzie V = 2 * n + 2
# Zlozonosc pamieciowa: O(V)

from zad6testy import runtests
from collections import deque


def BFS(graph, s, t):
    visited = [False for _ in range(len(graph))]
    parents = [None for _ in range(len(graph))]
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        u = q.popleft()
        for v in graph[u]:
            if visited[v] == False:
                q.append(v)
                visited[v] = True
                parents[v] = u
                if v == t:
                    return 1, parents

    return 0, parents


def getGraph(M, t):
    graph = []

    graph.append([i + 1 for i in range(len(M))])

    for elem in M:
        graph.append([node + len(M) + 1 for node in elem])

    for _ in range(len(M)):
        graph.append([t])

    graph.append([])

    return graph


def binworker(M):
    s = 0
    t = 2 * len(M) + 1
    ret = 0

    graph = getGraph(M, t)

    while True:
        flow, parents = BFS(graph, s, t)

        if not flow:
            break

        ret += flow

        v = t
        while v != s:
            u = parents[v]
            graph[u].remove(v)
            graph[v].append(u)
            v = u

    return ret


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)
