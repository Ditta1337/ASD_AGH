import math


def printTab(tab):
    length = len(tab)
    for i in range(length - 1):
        print(tab[i], end=", ")
    print(tab[length - 1])


def heapify(tab, length, index):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index

    if left <= length and tab[left] > tab[index]:
        largest = left
    if right <= length and tab[right] > tab[largest]:
        largest = right
    if largest != index:
        tab[index], tab[largest] = tab[largest], tab[index]
        heapify(tab, length, largest)


def buildMaxHeap(tab, length):
    for i in range(length // 2, -1, -1):
        heapify(tab, length, i)


def heapsort(tab):
    length = len(tab) - 1
    buildMaxHeap(tab, length)
    for i in range(length, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        length -= 1
        heapify(tab, length, 0)


if __name__ == "__main__":
    tab = [1, 2, 1]
    printTab(tab)
    heapsort(tab)
    printTab(tab)
