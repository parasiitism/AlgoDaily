from heapq import *

"""
    1st: 

    Time    O((E+V)logV)
"""


class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        marked_set = set(marked)
        G = defaultdict(list)
        for u, v, w in edges:
            G[u].append((v, w))
        pq = [(0, s)]
        seen = {}
        while len(pq) > 0:
            cost, node = heappop(pq)

            if node in seen and cost >= seen[node]:
                continue
            seen[node] = cost

            if node in marked_set:
                return cost
            for nb, w in G[node]:
                heappush(pq, (cost+w, nb))
        return -1
