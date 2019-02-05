import heapq


def warehouseMinCost(edges):
    """
    Your are given a list of routes, <warehouseA, warehouseB, cost>,
    write a function to return a collections which go through all the warehouses with minimum cost.

    Idea: Prim

    input:
    - edges: an array of edges, (warehouse1, warehouse2, cost)

    return:
    - a colletion of edges which connect all the warehouses

    Cautions
    - u r given all the edges
    - ids are numbers/strings
    - we are sure that all the edges belong to the same set/cluster
    """
    res = []
    visited = {}
    pq = []
    # pick the first vertex as a starting point
    start = edges[0][0]
    visited[start] = True
    for edge in edges:
        if edge[0] == start or edge[1] == start:
            heapq.heappush(pq, (edge[2], edge[0], edge[1]))
    while len(pq) > 0:
        cost, a, b = heapq.heappop(pq)
        found1 = False
        found2 = False
        if a in visited:
            found1 = True
        if b in visited:
            found2 = True
        if found1 and found2:
            continue
        elif found1:
            visited[b] = True
            res.append((a, b, cost))
            for edge in edges:
                if edge[0] == b or edge[1] == b:
                    heapq.heappush(pq, (edge[2], edge[0], edge[1]))
        elif found2:
            visited[a] = True
            res.append((a, b, cost))
            for edge in edges:
                if edge[0] == a or edge[1] == a:
                    heapq.heappush(pq, (edge[2], edge[0], edge[1]))
    return res


a = [(1, 2, 4),
     (1, 6, 2),
     (2, 6, 5),
     (2, 3, 6),
     (3, 6, 1),
     (4, 5, 2),
     (5, 6, 4),
     (3, 4, 3)]

print(warehouseMinCost(a))

a = [('a', 'b', 4),
     ('a', 'f', 2),
     ('b', 'f', 5),
     ('b', 'c', 6),
     ('c', 'f', 1),
     ('d', 'e', 2),
     ('e', 'f', 4),
     ('c', 'd', 3)]

print(warehouseMinCost(a))
