import heapq

"""
    dijkstra on a directed graph
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
    # time (from, to , cost)
    for src, dest, cost in edges:
        if src in connections:
            connections[src].append((src, dest, cost))
        else:
            connections[src] = [(src, dest, cost)]
    # dijkstra's
    heap = [(0, p, [])]
    best = {}
    while len(heap) > 0:
        # pop the edge with min cost
        cost, fromLoc, visited = heapq.heappop(heap)
        # if the cost < calculated cost of the node, update the node
        if fromLoc in best and cost >= best[fromLoc][0]:
            continue
        best[fromLoc] = (cost, visited)
        # add the adjacent nodes to the pq for processing
        if fromLoc in connections:
            candidates = connections[fromLoc]
            for can in candidates:
                heapq.heappush(heap, (cost+can[2], can[1], visited+[can[0]]))

    return best[q][1]


# normal case: https://www.youtube.com/watch?v=_lHSawdgXpI
r = [
    ['A', 'B', 4],
    ['A', 'C', 2],
    ['B', 'C', 3],
    ['C', 'B', 1],
    ['B', 'D', 2],
    ['B', 'E', 3],
    ['C', 'D', 4],
    ['C', 'E', 6],
    ['D', 'E', 1],
]
print(dijkstra(r, 'A', 'E'))
