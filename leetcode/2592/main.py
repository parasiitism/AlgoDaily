"""
    sort + 2 pointers

    Time    O(NlogN)
    Space   O(1)
"""


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        j = 0
        for i in range(n):
            x = nums[i]
            while j < n and nums[j] <= x:
                j += 1
            if j < n:
                res += 1
                j += 1
        return res
