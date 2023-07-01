# Artur Dwornik

# T_tab to tablica z kosztami zaparkowania, gdy nie uzywamy podwojonego czasu
# Tp_tab to tablica z kosztami zaparkowania, gdy uzywamy podwojonego czasu na drodze
# T_tab[i] = min(T_tab[i - j] + C[i]) dla j = 1, 2, ..., T
# Tp_tab[i] = min(min(Tp_tab[i - j] + C[i]), min(T_tab[i - k] + C[i])) dla j = 1, 2, ..., T, k = 1, 2, ..., 2T
# Wynikiem jest Tp_tab(n - 1), gdzie n - 1 to indeks miasta B
# Gdy 2T >= L, to zwracamy 0, poniewaz uzywajac podwojnego czasu z A mozemy dostac sie prosto do B

# Zlozonosc obliczeniowa: O(n * T), gdzie n to liczba miast, a T to maksymalny czas na drodze
# 2T <= n, wiec zlozonosc wynosi O(n^2)                    
# Zlozonosc pamieciowa: O(n)


from zad9testy import runtests

def calculate(T_tab, Tp_tab, data, T):
    n = len(T_tab)

    for i in range(1, n):
        min_val_T = min_val_Tp = min_val_T_2  = float("inf")
        for j in range(1, T):
            ind = i - j
            if ind < 0 or data[ind][0] < data[i][0] - T : 
                break
            if T_tab[ind] + data[i][1] < min_val_T:
                min_val_T = T_tab[ind] + data[i][1]

            if Tp_tab[ind] + data[i][1] < min_val_Tp:
                min_val_Tp = Tp_tab[ind] + data[i][1]

        for k in range(1, 2 * T):
            ind  = i - k
            if ind < 0 or data[ind][0] < data[i][0] - 2 * T:
                break

            if T_tab[ind] + data[i][1] < min_val_T_2:
                min_val_T_2 = T_tab[ind] + data[i][1]

        T_tab[i] = min_val_T
        Tp_tab[i] = min(min_val_Tp, min_val_T_2)


def min_cost( O, C, T, L ):
    if 2 * T >= L:
        return 0

    data = list(zip(O, C))
    data = sorted(data, key=lambda x: x[0])
    data.insert(0, (0, 0))
    data.append((L, 0))
    
    T_tab = [-1 for _ in range(len(O) + 2)]
    Tp_tab = [0 for _ in range(len(O) + 2)]

    T_tab[0] = 0

    calculate(T_tab, Tp_tab, data, T)

    return Tp_tab[-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
