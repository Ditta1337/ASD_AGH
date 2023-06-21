
# Find Bridges, O(V+E)

class Node():
    def __init__(self):
        self.visited_time = 0
        self.low = 0
        self.parent = None
        self.kids = []
        self.visited = False


#G = [(1, 6), (0, 2), (3, 6), (2, 4, 5), (3, 5), (3, 4), (0, 2, 7), (6)]
G = [(1), (0, 2, 3), (1, 5, 6), (1, 4), (3), (2, 7), (2, 7), (5, 6, 8), (7)]


def bridgeDFS(G, index, tab_of_nodes, time, ret):
    time += 1
    tab_of_nodes[index].visited = True
    tab_of_nodes[index].visited_time = time
    tab_of_nodes[index].low = time
    if type(G[index]) == int:
        if not tab_of_nodes[G[index]].visited:
            tab_of_nodes[index].kids.append(G[index])
            tab_of_nodes[G[index]].parent = index
            bridgeDFS(G, G[index], tab_of_nodes, time, ret)
    else:
        for elem in G[index]:
            if not tab_of_nodes[elem].visited:
                tab_of_nodes[index].kids.append(elem)
                tab_of_nodes[elem].parent = index
                bridgeDFS(G, elem, tab_of_nodes, time, ret)

    if type(G[index]) == int:
        if tab_of_nodes[index].parent != None:
            ret.append((tab_of_nodes[index].parent, index))
    else:
        elem_time = tab_of_nodes[index].visited_time
        the_elem = index
        for elem in G[index]:
            if tab_of_nodes[index].parent != elem and tab_of_nodes[elem].visited_time < elem_time:
                elem_time = tab_of_nodes[elem].visited_time
                the_elem = elem
        kids = tab_of_nodes[index].kids
        if kids == []:
            kids_low = 9**9
        else:
            kids_low = tab_of_nodes[kids[0]].low
            for kid in kids:
                if tab_of_nodes[kid].low < kids_low:
                    kids_low = tab_of_nodes[kid].low
        tab_of_nodes[index].low = min(
            tab_of_nodes[index].visited_time, tab_of_nodes[the_elem].visited_time, kids_low)
        if tab_of_nodes[index].low == tab_of_nodes[index].visited_time and tab_of_nodes[index].parent != None:
            ret.append((tab_of_nodes[index].parent, index))


def findBridge(G):
    n = len(G)
    time = 0
    ret = []
    tab_of_nodes = [Node() for _ in range(n)]

    for index in range(n):
        if not tab_of_nodes[index].visited:
            bridgeDFS(G, index, tab_of_nodes, time, ret)
    print("Mosty:", ret)


findBridge(G)
