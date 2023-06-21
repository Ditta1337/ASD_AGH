class Node:
    def __init__(self):
        self.val = None
        self.next = None

    def print(self):
        while self.next != None:
            print(self.val, end=", ")
            self = self.next
        print(self.val)


def tabToList(tab):
    length = len(tab)
    next = None

    for i in range(length-1, -1, -1):
        elem = Node()
        elem.val = tab[i]
        elem.next = next
        next = elem
    return next


def lenOfList(LL):
    if LL.next == None:
        return 0
    counter = 0
    while LL.next != None:
        counter += 1
        LL = LL.next
    return counter + 1


def getIndex(LL, index):
    for _ in range(index - 1):
        LL = LL.next
    return LL.val


def changeValue(LL, index, value):
    for _ in range(index - 1):
        LL = LL.next
    LL.val = value


def swap(LL, x, y):            # x, y = y, x
    tmp = getIndex(LL, x)
    changeValue(LL, x, getIndex(LL, y))
    changeValue(LL, y, tmp)


def heapify(LL, length, index):
    left = 2*index
    right = 2*index + 1
    largest = index

    if left <= length and getIndex(LL, left) > getIndex(LL, index):
        largest = left
    if right <= length and getIndex(LL, right) > getIndex(LL, largest):
        largest = right
    if largest != index:
        swap(LL, index, largest)
        heapify(LL, length, largest)


def buildMaxHeap(LL, length):
    for i in range(length//2, 0, -1):
        heapify(LL, length, i)


def heapsort(LL):
    length = lenOfList(LL)
    buildMaxHeap(LL, length)
    for i in range(length, 1, -1):
        swap(LL, 1, i)
        length -= 1
        heapify(LL, length, 1)


if __name__ == "__main__":
    tab = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    LL = tabToList(tab)
    LL.print()
    heapsort(LL)
    LL.print()
    # print(lenOfList(LL))
    #print(getIndex(LL, 6))
