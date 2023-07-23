"""
    1st: array

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        peak, dip = nums[0], nums[0]
        for x in nums:
            peak = max(peak, x)
            dip = min(dip, x)
        for x in nums:
            if x != peak and x != dip:
                return x
        return -1
