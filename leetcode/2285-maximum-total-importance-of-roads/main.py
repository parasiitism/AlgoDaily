from collections import *

"""
    hashtable + sort

    Time    O(NlogN)
    Space   O(N)
    1712 ms, faster than 66.67%
"""


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(int)
        for u, v in roads:
            g[u] += 1
            g[v] += 1
        pairs = []
        for node in g:
            cnt = g[node]
            pairs.append((node, cnt))
        pairs.sort(key=lambda x: -x[1])
        i = n
        scores = {}
        for node, cnt in pairs:
            scores[node] = i
            i -= 1
        res = 0
        for u, v in roads:
            importance = scores[u] + scores[v]
            res += importance
        return res
