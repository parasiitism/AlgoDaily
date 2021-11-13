"""
    1st: sort + binary search

    Time    O(IloI, QlogN)
    Space   O(I+Q)
    1508 ms, faster than 100.00%
"""


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: (x[0], x[1]))
        runningMaxes = []
        runningMax = -(2**32)
        for p, b in items:
            runningMax = max(b, runningMax)
            runningMaxes.append((p, runningMax))
        res = []
        for q in queries:
            i = self.lowerBsearch(items, q+1) - 1
            if i < 0:
                res.append(0)
            else:
                res.append(runningMaxes[i][1])
        return res

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid][0]:
                right = mid
            else:
                left = mid + 1
        return left
