from heapq import *
"""
    1st: maxheap
    - since the input array is sorted by x, i.e. xi < xj, for indices i < j
        yi + yj + |xi - xj|
        = yi + yj + xj - xi
        = (yi - xi) + (yj + xj)
    
    - it means we can only care about yi - xi for every index i
    - use maxheap

    Time    O(NlogN)
    Space   O(N)
    1248 ms, faster than 57.83%
"""


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        maxheap = []
        res = -(2**32)
        for x, y in points:
            # remove all xi that are < xj - k
            while len(maxheap) > 0 and maxheap[0][1] < x - k:
                heappop(maxheap)
            if len(maxheap) > 0:
                res = max(res, -maxheap[0][0] + y + x)  # (yi - xi) + (yj + xj)
            heappush(maxheap, (x - y, x))
        return res
