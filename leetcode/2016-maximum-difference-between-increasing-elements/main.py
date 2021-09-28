"""
    1st: dynamic programming
    - similar to lc121: stock
    - but here i use a different way

    Time    O(N)
    Space   O(N)
    48 ms, faster than 92.31%
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = n * [0]
        maxFromRight = 0
        for i in range(n-1, -1, -1):
            maxFromRight = max(maxFromRight, nums[i])
            maxs[i] = maxFromRight
        res = -1
        for i in range(n):
            diff = maxs[i] - nums[i]
            if diff > 0:
                res = max(res, diff)
        return res
