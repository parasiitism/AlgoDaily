
from collections import *

"""
    1st: dynamic programming
    - for every point, try all possibilities to the end of the road
    - cache the gain at any point x to avoid redundant calculation

    Time    O(N^2)
    Space   O(N)
    3792 ms, faster than 100.00%
"""


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        ht = defaultdict(list)
        for s, e, t in rides:
            ht[s].append([e, t])

        cache = {}

        def f(s):
            if s == n:
                return 0
            if s in cache:
                return cache[s]

            res = f(s+1)
            for e, t in ht[s]:
                res = max(res, e-s+t+f(e))

            cache[s] = res
            return cache[s]

        return f(0)
