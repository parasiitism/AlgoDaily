import sys

"""
    1st: math

    Time    O(N)
    Space   O(N)
    112 ms, faster than 17.76%
"""


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mi = sys.maxsize
        ma = -sys.maxsize
        for a in A:
            mi = min(mi, a)
            ma = max(ma, a)

        lower = mi + K
        upper = ma - K

        if lower >= upper:
            return 0
        return upper - lower
