# Artur Dwornik

# Tworze tablice 2 x n x n w ktorej przechowuje najdluzsze sciezki
# W labiryncie zawsze oplaca sie poruszac pierwsze w gore lub w dol,
# a potem dopiero w prawo. Na kazdym polu znajduje sie dwuelementowa
# tablica, w kotrej przechowuje dlugosc sciezki idac w dol oraz idac
# w gore. Poczatkowymi wartosciami 'prawego' pokoju jest najwieksza
# wartosc sposrod tej dwuelementowej tablicy + 1. Nastepnie powtarzam
# proces idac w dol oraz w gore w sumie n razy (n = len(L)).
# Wynikiem jest najwieksza wartosc z pola tab[n-1][n-1], lub -1
# jezeli nie da sie dotrzec do pola koncowego.

# Zlozonosc obliczeniowa: O(n^2)
# Zlozonosc pamieciowa: O(n^2)

from zad7testy import runtests

def goDown(tab, L, i, n):
    for j in range(n - 1):
        if tab[j][i][0] >= tab[j+1][i][0] and L[j+1][i] != '#':
            tab[j+1][i][0] = tab[j][i][0] + 1
            
def goUp(tab, L, i, n):
    for j in range(n - 1, 0, -1):
        if tab[j][i][1] >= tab[j-1][i][1] and L[j-1][i] != '#':
            tab[j-1][i][1] = tab[j][i][1] + 1

def goRight(tab, L, i, n):
    if i == n - 1:
        return
    
    for j in range(n):
        max_val = max(tab[j][i])
        if L[j][i+1] != '#':
            tab[j][i+1][0] = max_val + 1
            tab[j][i+1][1] = max_val + 1


def maze( L ):
    n = len(L)
    tab = [[[-float('inf'), -float('inf')] for _ in range(n)] for _ in range(n)]
    tab[0][0] = [0, 0]

    for i in range(n):
        goDown(tab, L, i, n)
        goUp(tab, L, i, n)
        goRight(tab, L, i, n)

    ret = max(tab[n-1][n-1])

    return ret if ret != -float('inf') else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
