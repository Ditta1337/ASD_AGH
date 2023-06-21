# Artur Dwornik

# Rekurencyjnie zbieram cale pole ropy, nastepnie jade
# na tyle ile mi pozwala paliwo w baku, rownoczensie
# dodajac nowe miniete pola ropy do kolejki.
# Jezeli paliwo nam sie skonczylo przed meta, to wyciagamy
# najwieksze pole ropy z kolejki i 'dolewamy' je do baku,
# przypominajac sobie, ze faktycznie zatrzymywalismy sie
# przy nim, zeby je zebrac.

# n to dlugosc trasy, a m to glebokosc najglebszego pola ropy:
# Zlozonosc obliczeniowa: O(mn),
# Zlozonosc pamieciowa: O(n),    

from zad8testy import runtests
from queue import PriorityQueue

def getOil(T, n, m, i, j, vol):
    vol[0] += T[j][i] 
    T[j][i] = 0
    for dir in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        new_j = j + dir[0]
        new_i = i + dir[1]
        if new_i >= 0 and new_i < n and new_j < m and new_j >= 0 and T[new_j][new_i]:
            getOil(T, n, m, new_i, new_j, vol)
    return vol[0]


def plan(T):
    ret = 1
    m = len(T)
    n = len(T[0])
    vol = getOil(T, n, m, 0, 0, [0])
    i = 0
    q = PriorityQueue()

    while True:
        while vol:
            i += 1
            vol -= 1

            if i == n - 1:
                return ret
            
            if T[0][i]:
                new_vol = getOil(T, n, m, i, 0, [0])
                if new_vol:
                    q.put(-new_vol)
        
        ret += 1
        vol -= q.get()
    
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

