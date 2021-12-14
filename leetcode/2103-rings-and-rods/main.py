from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def countPoints(self, rings: str) -> int:
        ht = defaultdict(set)
        for i in range(0, len(rings), 2):
            color = rings[i]
            pos = rings[i+1]
            ht[pos].add(color)
        res = 0
        for key in ht:
            if len(ht[key]) == 3:
                res += 1
        return res
