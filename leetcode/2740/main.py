"""
    sort

    Time    O(NlogN)
    Space   O(1)
"""


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = 2**32
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            res = min(res, diff)
        return res
