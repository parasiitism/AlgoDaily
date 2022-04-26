from collections import *

"""
    Line Sweep + binary search
    - class question

    Time    O(F + FlogF + PlogF)
    Space   O(F)
    1444 ms, faster than 33.33%
"""


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        blooms = Counter()
        for s, e in flowers:
            blooms[s] += 1
            blooms[e+1] -= 1
        points = list(blooms.keys())
        points.sort()

        pfs = 0
        intvs = []
        for x in points:
            pfs += blooms[x]
            intvs.append([x, pfs])

        res = []
        for p in persons:
            idx = self.bSearchSmaller(intvs, p)
            res.append(intvs[idx][1])
        return res

    def bSearchSmaller(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid][0]:
                right = mid - 1
            elif target > nums[mid][0]:
                left = mid + 1
            else:
                return mid
        # to find number that <= target
        return right
