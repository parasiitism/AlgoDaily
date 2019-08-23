from collections import *

"""
    1st: hashtable

    e.g.
    [
        [1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1],
    ]

    we transform it to
    [
        [1,3,5],
        [3,4],
        [1,4],
        [2],
        [3,4],
        [1,4,5],
    ]

    Time    O(RC)
    Space   O(RC)
    172 ms, faster than 27.76% 
"""


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        m = defaultdict(int)
        for row in wall:
            pfs = 0
            for j in range(len(row)):
                if j + 1 == len(row):
                    continue
                col = row[j]
                pfs += col
                m[pfs] += 1
        maxNum = 0
        for key in m:
            maxNum = max(maxNum, m[key])
        return len(wall) - maxNum
