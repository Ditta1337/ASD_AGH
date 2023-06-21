# Dane: C = {0, ..., n-1} - zbior miast
# d = C x C -> R - metryka nad C
# Zadanie: znalezc trase zaczynajaca sie w miescie 0, przebiegajaca przez wszystkie inne miasta (przez kazde dokladnie raz),
#          wracajaca do miasta 0 o minimalnej sumarycznej dlugosci

# Algorytm bruteforce: sproboj kazdej kolejnosci odwiedzania miast. Czasowa: O(n! * n), Pamieciowa: O(n)

# Algorytm dynamiczny:

# 1. Funkcnje do obliczenia:
# S - podzbior miast, taki ze 0 nalezy do S oraz t nalezy do S
# f(S, t) = dlugosc (w sensie d) najkotszej trasy z miasta 0 do miasta t przebiegajacej przez wszystkie miasta z S
# Wynik: min(f(C, t) + d(t, 0)), t = {1, ..., n-1}

# 2. Sformulowanie rekurencyjne:
# f(S, t) = min(f(S-{t}, r) + d(r, t)), r nalezy do S-{t}
# f({0}, 0) = 0 - warunek brzegowy

# Zlozonosc: Czasowa: O(n^2 * 2^n), Pamieciowa: O(n * 2^n)
