from heapq import *

"""
    Graph
    1. For each node, run a Dijkstra
    2. In each Dijkstra, for the 'best'
        - for the city itself, store the appleCost only
        - for the rest of the cities, store the appleCost and travel cost (visiting + on the way back)
        - so the result will be the one amongst all the 'best'

    Time    O(N * NlogN)
    Space   O(N*N)
    2386 ms, faster than 55.00%
"""


class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        g = {}
        for i in range(n):
            g[i] = []
        for u, v, cost in roads:
            g[u-1].append((v-1, cost))
            g[v-1].append((u-1, cost))
        res = []
        for i in range(n):
            pq = [(0, i)]
            best = n * [2**32]  # 2)
            while len(pq) > 0:
                cost, node = heappop(pq)
                if appleCost[node]+(1+k)*cost > best[node]:
                    continue
                best[node] = appleCost[node]+(1+k)*cost
                for nb, c in g[node]:
                    heappush(pq, (cost + c, nb))
            res.append(min(best))
        return res
