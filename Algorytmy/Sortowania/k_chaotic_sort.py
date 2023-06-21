def min_heapify(tab, n, ind):

    left = 2 * ind + 1
    right = 2 * ind + 2
    smallest = ind

    if left < n and tab[left] < tab[ind]:
        smallest = left
    
    if right < n and tab[right] < tab[smallest]:
        smallest = right

    if smallest != ind:
        tab[ind], tab[smallest] = tab[smallest], tab[ind]
        min_heapify(tab, n, smallest)

def buildheap(tab, n):
    for i in range((n - 2) // 2, -1, -1):
        min_heapify(tab, n, i)

def heappush(tab, val):
    i = len(tab)
    tab.append(val)
    parent = (i - 1) // 2
    while parent >= 0 and tab[i] < tab[parent]:
        tab[i], tab[parent] = tab[parent], tab[i]
        i = parent
        parent = (i - 1) // 2

def heappop(tab):
    ret = tab[0]
    tab[0] = tab[len(tab) - 1]
    tab.pop()
    min_heapify(tab, len(tab), 0)

    return ret


def k_chaotic_sort(lst, k):
    heap = lst[:k+1]
    buildheap(heap, k+1)
    for i in range(k+1, len(lst)):
        heappush(heap, lst[i])
        lst[i-k-1] = heappop(heap)
    for i in range(len(lst)-k-1, len(lst)):
        lst[i] = heappop(heap)
    return lst
        
    return result


lst = [2, 6, 6, 10, 29, 24, 31, 43, 36, 45, 51, 49, 52, 56, 53, 56, 61, 58, 71, 75, 72, 79, 93, 82, 99]
k = 1
result = k_chaotic_sort(lst, k)
print(result)