def heapify(tab, i, n, ind): # O(log(n))
    left = 2 * i + 1
    right = 2 * i + 2
    max_ind = i

    if left < n and tab[left][ind] < tab[max_ind][ind]: max_ind = left
    if right < n and tab[right][ind] < tab[max_ind][ind]: max_ind = right

    if max_ind != i:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify(tab, max_ind, n, ind)

class PriorityQueue():
    def __init__(self, size):
        self.heap = []
        self.size = size

    def put(self, elem):
        heap = self.heap
        size = self.size
        n = len(heap)
        ind = n - 1
        if n < size:
            heap.append(elem)
        else:
            max_ind = -1
            max_val = elem[0]
            for i in range((n - 1), (n - 1) // 2, -1):
                if heap[i][0] > max_val:
                    max_ind = i
                    max_val = heap[i][0]
            if max_ind != -1:
                heap[max_ind] = elem
                ind = max_ind
        parent = (ind - 1) // 2
        while ind != 0 and heap[ind][0] < heap[parent][0]:
            heap[ind], heap[parent] = heap[parent], heap[ind]
            ind = parent
            parent = (ind - 1) // 2
    
    def get(self):
        heap = self.heap
        n = len(heap)

        if n == 0:
            return [-1, -1]
        
        ret = heap[0]
        if n == 1:
            heap.pop()
            return ret
        
        heap[0] = heap[n - 1]
        heap.pop(n - 1)
        heapify(heap, 0, n - 1, 0)

        return ret
        


def k_smallest_sums(nums1, nums2, k):
    ret = []
    queue = PriorityQueue(size=k)
    for num1 in nums1:
        for num2 in nums2:
            queue.put([num1 + num2, [num1, num2]])

    #queue.heap.pop(len(queue.heap) - 1)

    for _ in range(k):
        elem = queue.get()[1]
        if elem != -1:
            ret.append(elem)

    return ret


nums1 = [-10,-4,0,0,6]
nums2 = [3,5,6,7,8,100]
k = 10
print(k_smallest_sums(nums1, nums2, k))