import sys

"""
    1st: sort

    Time    O(NlogN)
    Space   O(N)
    364 ms, faster than 28.71% 
"""


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        minDiff = sys.maxsize
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            minDiff = min(minDiff, diff)
        res = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff == minDiff:
                res.append([arr[i-1], arr[i]])
        return res
