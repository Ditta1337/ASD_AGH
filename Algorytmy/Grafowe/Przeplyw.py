# Wejscie: G(V, E) - graf skierowany (krawedzie w jedna strone)
# c: V x V -> N - pojemnosci krawedzi
# jesli (u, v) not in E -> c(u, v) = 0
# Zadanie: znalezc przeplyw f o maksymalej wartosci, gdzie
# przeplyw f. V x V -> N, 
# s - zrodlo, brak krawedzi wchodzacych
# t - wyjscie, brak krawedzi wychodzacych
# for every u, v: (f(u,v) <= c(u,v))
# for every v in V \ {s, t}: (sum(f(u,v)) for u in V == sum(f(v, u))) for u in V)
# |f| = sum(f(s, v)) for v in V - sum(f(v, s)) for v in V
#                                 -----------0-----------

# Sieci residualne:
# G = (V, E), s, t in V     | siec przeplywowa
# c: V x V -> N             |
# f: V x V -> N
# Siec residualna ujmuje pojemnosci oraz aktualny przelowyw, daje 
# infrmacje jaki jeszcze przeplyw mozemy jeszcze przepuscic

# Definiujemy siec residualna Gf, Cf przez funkce Cf:
# Cf(u, v) = | c(u, v) - f(u, v), (u, v) in E
#            | f(v, u), (v, i) in E
#            | 0, w.p.p.

# Sciezka powiekszajaca dla Gf to siezka z s do t w Gf, Cf.
# Wartoscia tej siezki jest najmniejsza wartosc Cf(u, v) na sciezce
# Szukamy takiej sciezki BFS albo DFS i wyznaczenie minimum.

# Metoda Forda-Fulkersona: O((V + E)     *     |f*| )      =    O(E|f*|)
#                            --BFS--  -wartosc max przeplywu-
#                            --DFS--  -wartosc max przeplywu-
# czas dzialania mozna stanowczo przyspieczyc wyszukujac sciezke 
# powiekszajaca metoda BFS => Algorytm Elmondsa-Karpa O(VE^2)     !!!! 
# 1. Jesli istnieje sciezka powiekszajaca dla Gf, Cf, to powieksz
# zgodnie z nia przeplyw.
# 2. Wroc do kroku 1.

# Przekroj w sieci:
# G(V, E), s, t    |siec przeplywowa
# c: V x V -> N    |
# f: V x V -> N
# Przekroj sieci to podzial V na
# S, V-S = T, gdzie s in S, t in T
# Przepustowosc przekroju S, T: 
# c(S, T) = sum(sum(c(u, v)) for v in T) for u in S

# Przeplyw netto:
# f(S, T) = sum(sum(f(u, v)) for v in T) for u in S - sum(sum(f(v, u)) for v in T) for u in S

# Kilka wariantów problemu:
# 1. Krawedzie w obie strony
# 2. Wiele zrodel i wiele ujsc: O(VE) - metoda Forda-Fulkersona
#    - tworzymy super zrodlo z inf pojemnoscia do kazdego ze zrodlem
#    - tworzymy super ujscie z inf pojemnoscia od kazdego ujscia
# 3. Maksymane skojarzenie w grafie dwudzielnym:
#    - tworzymy zrodlo s prowadzace do wierzcholkow po lewej o wartosci 1
#    - kazda krawedz w grafie dwudzielnym ma pojemnosc 1
#    - tworzymy ujscie t prowadzace do wierzcholkow po prawej o wartosci 1