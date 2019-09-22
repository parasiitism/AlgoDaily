import heapq
from collections import defaultdict


def warehouseMinCost(edges):
    """
    Your are given a list of routes, <warehouseA, warehouseB, cost>,
    write a function to return a collections which go through all the warehouses with minimum cost.

    input:
    - edges: an array of edges, (warehouse1, warehouse2, cost)
    - warehouse1, warehouse2 are strings
    - cost is number
    - edges are undirected, guarantee that there will be no duplicate routes

    return:
    - a colletion of edges which connect all the warehouses
    - if there are no edges connected to all the nodes, return an empty array

    2nd attempt: Prim

    Cautions
    - u r given all the edges
    - ids are numbers/strings
    """
    if len(edges) == 0:
        return []
    visited = {}
    for edge in edges:
        visited[edge[0]] = False
        visited[edge[1]] = False
    res = []
    pq = []
    # establish connections table
    connections = defaultdict(list)
    for a, b, cost in edges:
        connections[a].append((a, b, cost))
        connections[b].append((b, a, cost))
    # pick the first vertex as a starting point
    start = edges[0][0]
    visited[start] = True
    for edge in edges:
        if edge[0] == start or edge[1] == start:
            heapq.heappush(pq, (edge[2], edge[0], edge[1]))
    # always get the edge with smallest route from the min-heap
    while len(pq) > 0:
        cost, a, b = heapq.heappop(pq)
        foundA = visited[a]
        foundB = visited[b]
        # put the ajacent nodes into the min-heap
        if foundA and foundB:
            continue
        elif foundA:
            visited[b] = True
            res.append((a, b, cost))
            for edge in connections[b]:
                heapq.heappush(pq, (edge[2], edge[0], edge[1]))
        elif foundB:
            visited[a] = True
            res.append((a, b, cost))
            for edge in connections[b]:
                heapq.heappush(pq, (edge[2], edge[0], edge[1]))

    # if there is any unvisited node, it means there is no edge can reach to the node, therefore return []
    for key in visited:
        if visited[key] == False:
            return []

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

a = [('a', 'b', 4),
     ('a', 'f', 2),
     ('b', 'f', 5),
     ('b', 'c', 6),
     ('c', 'f', 1),
     ('d', 'e', 2),
     ('e', 'f', 4),
     ('c', 'd', 3),
     ('g', 'h', 1),
     ]

print(warehouseMinCost(a))
