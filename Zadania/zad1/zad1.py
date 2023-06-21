# Artur Dwornik
#
# Prosty algorytm, który n - 2 (n - 2 poniewaz na krańcach znajduje się palindrom o długści 1) razy wybiera
# "środek", po czym sprawdza w pętli, czy znaki po lewej od środa równają się tym po prawej od środka,
# z kazda iteracją pętli zwiększając promień o 1, dodaje do licznika 2, przy czym sprawdzając, czy nie 
# wychodzimy poza tablicę. Takim sposobem na pewno nie wybierzemy palindormu długości parzystej.
#
# Złozonosc obliczeniowa:
# W najgorszym przypadku (te same znaki w całym słowie):
#          (n//2)
# f(n) ≈ 2 * Σ  = n * (n + 2) / 4 => Θ(n) = n^2
#          i = 1

from zad1testy import runtests

def ceasar( s ):
    n = len(s)
    ret = 1

    for i in range(1, n - 1):
        counter = 1
        left = i - 1
        right = i + 1
        
        while left >= 0 and right <= n - 1 and s[left] == s[right]:
            counter += 2
            left -= 1
            right += 1

        ret = max(ret, counter)

    return ret

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
