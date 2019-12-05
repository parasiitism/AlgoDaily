"""
    1st: brute-force all cases

    Time    O(N) N: number of intervals
    Space   O(N)
    340 ms, faster than 84.52%
"""


class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for start, end in intervals:
            if start >= toBeRemoved[0] and end <= toBeRemoved[1]:
                continue
            elif end <= toBeRemoved[0] or start >= toBeRemoved[1]:
                res.append([start, end])
            elif start < toBeRemoved[0] and end > toBeRemoved[1]:
                res.append([start, toBeRemoved[0]])
                res.append([toBeRemoved[1], end])
            elif start < toBeRemoved[1] and end > toBeRemoved[1]:
                res.append([toBeRemoved[1], end])
            elif start < toBeRemoved[0] and end > toBeRemoved[0]:
                res.append([start, toBeRemoved[0]])
        return res
