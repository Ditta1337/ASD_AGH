from random import randint

def partition(tab, l, r, ind): # O(n * N / n) = O(N)
    def condition(tab, j, x):
        if ind == 0:
            second_ind = 1
            return tab[j][ind] == x[ind] and tab[j][second_ind] >= x[second_ind]
        else:
            second_ind = 0
            return tab[j][ind] == x[ind] and tab[j][second_ind] <= x[second_ind]
        
    random_num = randint(l, r)
    tab[r], tab[random_num] = tab[random_num], tab[r]
    x = tab[r]
    i = l - 1
    for j in range(l, r): 
        if tab[j][ind] < x[ind] or condition(tab, j, x):
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1

def quicksort(tab, l, r, ind): # O(N * log(n))
    while l < r:
        pivot = partition(tab, l, r, ind)
        quicksort(tab, l, pivot - 1, ind)
        l = pivot + 1

def binsearch_L(tab, elem, i):
    ret = -1
    start = 0
    stop = len(tab) - 1
    while start <= stop:
        mid = (stop + start) // 2
        if elem < tab[mid][i]:
            stop = mid - 1
        elif elem > tab[mid][i]:
            start = mid + 1
        else:
            ret = mid
            stop = mid - 1
    return ret


def max_contained_intervals(intervals):
    quicksort(intervals, 0, len(intervals) - 1, 0)
    sorted_start = [elem for elem in intervals]
    quicksort(intervals, 0, len(intervals) - 1, 1)
    sorted_end = intervals

    ret = 0
    for i, elem in enumerate(sorted_start):
        y = binsearch_L(sorted_end, elem[1], 1)
        ret = max(ret, y - i)
    
    print(ret)


 
intervals = [[0, 4], [2, 6], [2, 7], [5,6], [-1, 10]]
max_contained_intervals(intervals)