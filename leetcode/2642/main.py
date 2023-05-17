from heapq import *

"""
    1st: dijsktra

    Time    O((E+V)logV)
    Space   O(V)
"""


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.G = defaultdict(list)
        for u, v, c in edges:
            self.G[u].append((v, c))

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.G[u].append((v, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        best = {}
        pq = [(0, node1)]
        while len(pq) > 0:
            cost, node = heappop(pq)
            if node in best and cost > best[node]:
                continue
            best[node] = cost
            if node in self.G:
                for nb, c in self.G[node]:
                    heappush(pq, (cost + c, nb))
        if node2 in best:
            return best[node2]
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
