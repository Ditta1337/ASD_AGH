# Algorytm Floyda-Warshalla O(V^3)
# G: (V, E), w: V x V -> R, V = {v1, v2, ...}
# Idea: Jesli dla pewnego k znamy najkrotrsze sciezki miedzy kazda para
# wierzcholkow, ale ograniczone do wierzcholkow wewnetrznych tych sciezek
# ze zbioru {v1, ... ,vk-1} to mozemy latwo obliczyc najkrotsze sciezki
# z wierzcholkami wewnetrznymi od {v1, ..., vk}

# Konwencja: D(t)[u][v] - dlugosc najkrotrszej sciezki od u do v jesli
# po drodze mozna korzystac z wierzcholkow {v1, ..., vt}

A = [[0, 5, 999, 10],
     [999, 0, 3, 999],
     [999, 999, 0, 1],
     [999, 999, 999, 0]]


def FloydWarshall(A):
    n = len(A)
    D = A
    for k in range(n):
        for u in range(n):
            for v in range(n):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])

    for i in range(n):
        for j in range(n):
            print(D[i][j], end=' ')
        print()


FloydWarshall(A)
