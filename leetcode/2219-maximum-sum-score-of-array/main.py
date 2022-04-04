"""
    1st: prefix sum + suffix sum

    Time    O(N)
    Space   O(1)
    610 ms, faster than 100.00%
"""


class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        sfs = sum(nums)
        n = len(nums)
        pfs = 0
        res = -(2**32)
        for i in range(n):
            x = nums[i]
            pfs += x
            res = max(res, pfs, sfs)
            sfs -= x
        return res
