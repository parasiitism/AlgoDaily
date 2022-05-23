"""
    sort, find the max diff between numbers

    Tmie    O(NlogN)
    Space   O(N)
    1057 ms, faster than 28.57%
"""


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        nums = [bottom] + special + [top]
        res = 0
        for i in range(1, len(nums)):
            diff = 0
            if i == 1 or i == len(nums) - 1:
                diff = max(0, nums[i] - nums[i-1])
            else:
                diff = max(0, nums[i] - nums[i-1] - 1)
            res = max(res, diff)
        return res
