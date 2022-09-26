"""
    logic?
    - Bitwise AND of two numbers -> if 2 numbers are the same, their AND is the largest
    - so the Q becomes: find the longest subarray which includes only the max

    Time    O(N)
    Space   O(1)
    2403 ms, faster than 20.00%
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        largest = max(nums)
        res = 0
        cur = 0
        for x in nums:
            if x == largest:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        return res
