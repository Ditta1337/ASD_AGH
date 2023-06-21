# Artur Dwornik

# Tablicę ze śniegiem sortujemy heapsortem z min-heapem, tworząc tablicę
# posortowaną malejąco. Następnie jezeli snieg sie calkowicie nie stopil,
# to dodajemy jego wartosc (startowa - #dni pracy) do sumy wynikowej.
# Z racji, ze kazdego dnia snieg topnieje o 1 z kazdego pola to kolejnosc
# w ktorej zebieramy snieg jest nie wazna, a informacja, ze maszyna topi
# snieg po ktorym przejedzie jest 'baitem'.

# Złozonosc obliczeniowa:
# nlog(n) + n => O(nlog(n))

from zad2testy import runtests

def heapify(tab, i, n): # O(log(n))
    left = 2 * i + 1
    right = 2 * i + 2
    max_ind = i

    if left < n and tab[left] < tab[max_ind]: max_ind = left
    if right < n and tab[right] < tab[max_ind]: max_ind = right

    if max_ind != i:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify(tab, max_ind, n)

def build_min_heap(tab, n): # O(n)
    for i in range((n - 2) // 2, -1, -1):
        heapify(tab, i, n)

def heapsort(tab): # O(nlog(n))
    n = len(tab)
    build_min_heap(tab, n)
    for i in range(n - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, 0, i)


def snow( S ):
    ret = 0

    heapsort(S)
    for day, amount in enumerate(S):
        if day < amount:
            ret += amount - day

    return ret

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
