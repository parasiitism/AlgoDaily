
from collections import *

"""
    1st: line sweeping + merge intervals

    Time    O(N + NlogN)
    Space   O(N)
    1292 ms, faster than 100.00%
"""


class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = Counter()
        counts = Counter()

        # line sweeping
        for s, e, h in buildings:
            heights[s] += h
            counts[s] += 1
            heights[e] -= h
            counts[e] -= 1

        # merge intervals
        keys = sorted(heights.keys())
        curHegiht = heights[keys[0]]
        curCount = counts[keys[0]]
        prevCount = 0
        res = []
        for i in range(1, len(keys)):
            _k = keys[i-1]
            k = keys[i]
            if curCount > 0:
                avg = curHegiht//curCount
                if len(res) > 0 and avg == res[-1][2] and prevCount > 0:
                    res[-1][1] = k
                else:
                    res.append([_k, k, avg])
            prevCount = curCount
            curHegiht += heights[k]
            curCount += counts[k]

        return res
