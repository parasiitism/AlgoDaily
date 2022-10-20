from bisect import *

"""
    1st: sort + 2 pointers

    Time    O(NlogN + N)
    Space   O(1)
    183 ms, faster than 100.00%
"""


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        idx = bisect_left(nums, 0)
        L, R = idx-1, idx
        while L >= 0 and R < len(nums):
            left = abs(nums[L])
            right = nums[R]
            if left < right:
                L -= 1
            elif left > right:
                R += 1
            else:
                res = right
                L -= 1
                R += 1
        return res
