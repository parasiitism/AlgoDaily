"""
    1st: array

    Time    O(N)
    Space   O(N)
    80 ms, faster than 100.00%
"""


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = nums[i]
            if i % 10 == x:
                return i
        return -1
