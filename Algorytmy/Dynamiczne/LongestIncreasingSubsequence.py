#O(n^2), da sie O(nlogn)

# Dane: A[0, ..., n-1] - tablica liczb (niekoniecznie spójny ciąg)
# np: 2 (1) 4 (3) (4) 8 (5) (7)

# 1. Ustalamy funkcję, która bedziemy obliczac
# f(i) = dłgosc najdluzszego rosnacego podciagu w tablicy A[0, ..., i], konczacego sie liczba A[i]
# wynik: max(f(i)), i: 0, 1, 2, ..., n-1
#        wypisz ten ciag

# 2. Wyrażenie funkcji f w postaci rekurencyjnej
# f(i) = max(f(j) + 1 | j < i oraz A[j] < A[i])
# f(0) = 1 warunek brzegowy

# 3. Implementacja

def lis(A):
    n = len(A)
    maxIndex = 0
    F = [1 for i in range(n)] #tworzymy tablice przetrzymujaca wyniki z warotosciamy brzegowymi
    P = [-1 for i in range(n)] #tworzymy tablice indeksow do zwrocenia ciagu


    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    
        if F[i] > F[maxIndex]:
            maxIndex = i

    #return F[maxIndex] #zwraca dlugosc najdluzszego rosnacego ciagu
    return maxIndex, F, P

def printSol(A, P, i): #i = maxIndex
    if P[i] != -1:
        printSol(A, P, P[i])
    print(A[i])

