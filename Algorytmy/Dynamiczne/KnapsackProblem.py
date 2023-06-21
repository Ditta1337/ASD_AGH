# Dane: I = {0, ..., n-1} - przedmioty
# w: kazdemu przedmiotowi przypisuje wage
# p: kazdemu elementowi przypisuje cene/profit
# B: maksymalna waga

# Zadanie: znalezc podzbior I o maksymalnej sumarycznej cenie i lacznej wadze nie przekraczajacej B

# 1. Funkcje od obliczenia:
# f(i, b) = maksymalna suma cen przedmiotów ze zbioru {0, i}, nie przekraczajacych wagi b
# wynik: f(n - 1, B)

# 2. Sformulowanie rekurencyjne:
# f(i, b) = max(f(i - 1, b), f(i - 1, b - w(i)) + p(i)), b - w(i) >=0
#             nie bierzemy           bierzemy
# f(0, b) = p(0) <=> w(0) <= b
#         = 0    <=> w(0) > b

# 3. Implementacja :

def knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range (B+1)] for i in range(n)]

    for b in range(W[0], B+1): #pisujemy wartosci brzegowe
        F[0][b] = P[0]
    
    for b in range(B+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if b-W[i] >= 0:
                F[i][b] = max(F[i - 1][b], F[i - 1][b - W[i]] + P[i])

    return F[n-1][B]