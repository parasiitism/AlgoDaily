from collections import *

"""
    1st: hashtable + math?

    Time    O(N^2) worst
    Space   O(N)
    36 ms, faster than 91.67%
"""


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ht = defaultdict(list)
        for i in range(len(colors)):
            c = colors[i]
            ht[c].append(i)
        res = 0
        for key1 in ht:
            for key2 in ht:
                if key1 == key2:
                    continue
                firstIdx = ht[key1][0]
                lastIdx = ht[key2][-1]
                diff = abs(lastIdx - firstIdx)
                res = max(res, diff)
        return res
