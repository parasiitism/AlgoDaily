"""
    prefix sum

    Time    O(N)
    Space   O(N)
    1570 ms, faster than 60.00%
"""


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        pfs = 0
        pfss = []
        for i in range(n):
            pfs += nums[i]
            pfss.append(pfs)
        res = 0
        for i in range(n-1):
            left = pfss[i]
            right = total - left
            if left >= right:
                res += 1
        return res
