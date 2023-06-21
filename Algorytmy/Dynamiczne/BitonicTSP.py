# Wersja problemy w której:
# - miasta to punkty w przestrzeni R^2 (zadne dwa miasta nie maja tej samej wspolzednej x)
# - miasto 0 jest skrajnie po lewej (najmniejsza wspolzedna x)
# - szukamy trasy, ktora przebiega z lewa na prawo i z powortem (kierunek na osi x zmieniamy dokladnie raz)

# Algorytm dynamiczny:
# 1. Funkcje do obliczenia:
# f(i, j) = minimalny koszt sciezek z 0 do i oraz z 0 do j, ktore uzywaja lacznie wszystkich miast z {0, j}, ale zadnego nie powtazajac, i < j
# Wynik: min(f(i, n - 1) + d(i, n - 1))

# 2. Sformulowanie rekurencyjne:
# f(0, 1) = d(0, 1) - warunek brzegowy
# rozwarzamy dwa przypadki:
# a) f(i, j) = f(i, j - 1) + d(j - 1, j)
#   i < j - 1
# b) f(j - 1, j) = min(f(k, j - 1) + d(k, j))
#     k < j - 1
# 3. Implementacja:

from math import inf

#n = len(A) #lista z miastami
#D[i][j] = d(i, j) #odleglosci pomiedzy miastami
#F = [[inf for j in range(n)]for i in range(n)]

def tspf(i, j, F, D): #rekursja ze spamietywaniem
    if F[i][j] != inf:
        return F[i][j]
    
    if i == j - 1:   #b)
        best = inf
        for k in range(j-1):
            best = min(best, tspf(k, j-1, F, D) + D([k][j]))
        F[j-1][j] = best
    else:   #a) 
        F[i][j] = tspf(i, j - 1, F, D) + D[j-1][j]
    
    return F[i][j]



