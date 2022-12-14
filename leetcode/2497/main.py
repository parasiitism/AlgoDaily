"""
    graph
    
    Time    O(E+N)
    Space   O(N)
"""


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        g = defaultdict(list)
        for u, v in edges:
            g[u].append((vals[v], v))  # (value, nodeidx)
            g[v].append((vals[u], u))
        res = -2**32
        for nodeIdx in range(n):
            nbs = g[nodeIdx]
            nbs.sort(key=lambda x: -x[0])
            # only consider the values which > 0
            # don't forget to add the value of node itself
            temp = sum([max(a, 0) for a, _b in nbs[:k]]) + vals[nodeIdx]
            res = max(res, temp)
        return res
