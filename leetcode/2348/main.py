"""
    math

    Time    O(N)
    Space   O(1)
    1731 ms, faster than 20.00%
"""


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        cur = 0
        for i in range(n):
            x = nums[i]
            if x == 0:
                cur += 1
                res += cur
            else:
                cur = 0
        return res
