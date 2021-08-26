from heapq import *
from collections import *
from math import *

"""
    1st: dijkstra + dynamic programming

    Time    O((E + V)logV + V^2)
    Space   O(V)
    LTE ???
"""


class Solution(object):
    def countPaths(self, n, edges):
        # edge with cost { from: (to, cost), ... }
        connections = defaultdict(list)
        for a, b, cost in edges:
            connections[a].append((b, cost))
            connections[b].append((a, cost))
        minCost = self.dijkstra(n, connections)
        # print(minCost)
        res = self.dfs(n, 0, minCost, connections, {})
        return res

    def dfs(self, n, node, remainingCost, connections, ht):
        if remainingCost == 0:
            if node == n-1:
                return 1
            return None
        if remainingCost < 0:
            return None
        if node not in connections:
            return None
        key = (node, remainingCost)
        if key in ht:
            return ht[key]
        ways = 0
        for cand in connections[node]:
            nb, cost = cand
            temp = self.dfs(n, nb, remainingCost - cost, connections, ht)
            if temp != None:
                ways += temp
        ways %= 10**9 + 7
        ht[key] = ways
        return ways

    def dijkstra(self, n, connections):
        minheap = [(0, 0)]  # (cost, toNode)
        best = {}
        while len(minheap) > 0:
            cost, node = heappop(minheap)
            if node in best and cost >= best[node]:
                continue
            best[node] = cost
            if node in connections:
                candidates = connections[node]
                for cand in candidates:
                    heappush(minheap, (cost + cand[1], cand[0]))
        # print(best)
        return best[n-1]


"""
    2nd: dijkstra variation
    - learned from others

    ref:
    - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/discuss/1417576/C%2B%2BPython-Dijkstra-Clean-and-Concise

    Time    O((E + V)logV)
    Space   O(V)
    296 ms, faster than 97.88%
"""


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        # edge with cost { from: (to, cost), ... }
        connections = defaultdict(list)
        for a, b, cost in edges:
            connections[a].append((b, cost))
            connections[b].append((a, cost))
        minheap = [(0, 0)]  # (cost, toNode)
        best = n * [inf]
        ways = n * [0]
        best[0] = 0
        ways[0] = 1
        while len(minheap) > 0:
            cost, node = heappop(minheap)
            if cost > best[node]:
                continue
            if node not in connections:
                continue
            candidates = connections[node]
            for cand in candidates:
                nb, _cost = cand
                if cost + _cost < best[nb]:
                    best[nb] = cost + _cost
                    ways[nb] = ways[node]
                    heappush(minheap, (best[nb], nb))
                elif cost + _cost == best[nb]:
                    ways[nb] = (ways[nb] + ways[node]) % (10**9+7)
        # print(best)
        # print(ways)
        return ways[n-1]
