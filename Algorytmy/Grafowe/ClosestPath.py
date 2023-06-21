# 1. od v1 do reszty
# Podejscie elementarne:
# modyfikacja BFS - #krawedzie o dlugosci wiekszej niz 1 dzielimy
# na mniejsze krawedzie o dlugosci 1

# 2. od kazdego do kazdego
# V * Djikstra O(VElogV)
# V * BellmanFord O(V*2E)

# Konwencja: stosujemy implementacje macierzowa
# stosujemy macierz najkrotrszych odleglosci 
# D[u][v] - dl. najkrotszej sciezki od u do v
