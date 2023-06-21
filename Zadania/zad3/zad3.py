# Artur Dwornik
# Do nowej tablicy dodajemy wyrazy z T oraz takie odwrócone wyrazy, które nie są
# palindromami. Sortujemy tablicę quicksortem z losowym partition, a następnie iterujemy
# po posortowanej tablicy sumując te same wyrazy. Zwracamy największą sumę.
# Pierwszym moim pomysłem byla hashmapa ale działała dłuzej.

# Złozonosc obliczeniowa:
# O(N * log(n))

from zad3testy import runtests
from random import randint

def partition(tab, l, r): # O(n * N / n) = O(N)
    random_num = randint(l, r)
    tab[r], tab[random_num] = tab[random_num], tab[r]
    x = tab[r]
    i = l - 1
    for j in range(l, r): 
        if tab[j] >= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1

def quicksort(tab, l, r): # O(N * log(n))
    while l < r:
        pivot = partition(tab, l, r)
        quicksort(tab, l, pivot - 1)
        l = pivot + 1

def strong_string(T):
    ret = 0
    counter = 1
    T_new = []

    for word in T: # O(N)
        T_new.append(word)
        if word != word[::-1]:
            T_new.append(word[::-1])
    
    quicksort(T_new, 0, len(T_new) - 1)

    last = T_new[0]
    for i in range(1, len(T_new) - 1):
        if T_new[i] == last:
            counter += 1
            ret = max(counter, ret)
        else:
            last = T_new[i]
            counter = 1

    return ret


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
