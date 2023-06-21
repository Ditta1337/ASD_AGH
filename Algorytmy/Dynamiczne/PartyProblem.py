# Impreza jest dopuszczalna, jesli dla zadnego zaproszonego pracwonika nie zaporsilismy jego bezposredniego przelozonego
# Wartoscia imprezy jest suma wspolczynnikow 'fun' zaproszonych
# Zadanie: znalezc wartosc najelpszej dopuszczalnej imprezy

# 1. Okreslenie obliczanych funkcji:
# v - wezel drzewa
# f(v) - wartosc najlepszej imprezy poddrzewa zakorzenionego w v
# g(v) - -||-, pod warunkimem, ze v NIE IDZIE na impreze
# wynik: f(root)

# 2. Zaleznosci rekurencyjne
# g(v) = Σf(u), u - pracownik v
# f(v) = max(g(v), fun(v) + Σg(u)), u - pracownik v

# 3. Implementacja

class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = [] #tablica dzieci wezlow
        self.f = -1
        self.g = -1

def g(v): #rozwiazywanie ze spamietywaniem
    if v.g != -1:
        return v.g

    v.g = 0
    
    for u in v.emp:
        v.g += f(u)
    
    return v.g

def f(v): #rozwiazywanie ze spamietywaniem
    if v.f != -1:
        return v.f
    
    f1 = g(v)
    f2 = v.fun

    for u in v.emp:
        f2 += g(u)
    
    v.f = max(f1, f2)

    return v.f


