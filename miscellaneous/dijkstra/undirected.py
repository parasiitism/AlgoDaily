from heapq import *

"""
    dijkstra on a undirected graph

    Time    O((E + V) x logV)
    Space   O(V)
"""


def dijkstra(edges, p, q):
    """
    :type edges: List[List[int]]
    :type p: string, id for the start point
    :type q: string, id for the end point
    :rtype: [string], the path with min cost
    """
    # get all nodes
    nodeSet = set()
    for edge in edges:
        nodeSet.add(edge[0])
        nodeSet.add(edge[1])
    nodes = list(nodeSet)
    # adjacent list
    connections = {}
    # edge with cost { from: (to, cost), ... }
    for a, b, cost in edges:
        # from -> to
        if a in connections:
            connections[a].append((b, cost))
        else:
            connections[a] = [(b, cost)]
        # to -> from
        if b in connections:
            connections[b].append((a, cost))
        else:
            connections[b] = [(a, cost)]
    # dijkstra's
    # put (cost, node, parent) into the heap
    heap = [(0, p, None)]
    best = {}
    while len(heap) > 0:
        # pop the edge with min cost
        cost, node, parent = heappop(heap)
        # if the cost < calculated cost of the node, update the node
        if node in best and cost >= best[node][0]:
            continue
        best[node] = (cost, parent)
        # add the adjacent nodes to the pq for processing
        if node in connections:
            candidates = connections[node]
            for cand in candidates:
                heappush(heap, (cost+cand[1], cand[0], node))
    if q not in best:
        return [-1]
    # build the shortest path from the back by using the parent
    path = [q]
    cur = q
    while best[cur][1] != None:
        path.append(best[cur][1])
        cur = best[cur][1]

    return path[::-1]


# normal case: https://www.youtube.com/watch?v=_lHSawdgXpI
# but
# 1. change it to a undirected graph
# 2. change C-E from 5 to 4
r = [
    ['A', 'B', 4],
    ['A', 'C', 2],
    ['B', 'C', 3],
    ['B', 'D', 2],
    ['B', 'E', 3],
    ['C', 'D', 4],
    ['C', 'E', 4],
    ['D', 'E', 1],
]
print(dijkstra(r, 'A', 'E'))
