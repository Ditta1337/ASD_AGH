from queue import PriorityQueue

def merge_k_sorted_lists(lists):
    ret = []
    queue = PriorityQueue()
    for ind, list in enumerate(lists):
        queue.put([list[0], ind, 0])

    while not queue.empty():
        elem, list_ind, ind = queue.get()
        ret.append(elem)
        if ind + 1 < len(lists[list_ind]):
            queue.put([lists[list_ind][ind + 1], list_ind, ind + 1])

    return ret 




lists = [[1, 3, 6], [3, 5, 8], [10, 12, 15], [1]]

print(merge_k_sorted_lists(lists))

