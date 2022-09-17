from heapq import *

"""
    1st: heap
    - same as leetcode253

    Time    O(NlogN)
    Space   O(N)
    3253 ms, faster than 57.14%
"""


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minheap = []
        for s, e in intervals:
            if len(minheap) > 0 and s > minheap[0]:
                _smallest_group = heappop(minheap)
            heappush(minheap, e)
        return len(minheap)
