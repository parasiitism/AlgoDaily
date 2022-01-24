from collections import *

"""
    1st: array
    - the count the numbers they are not either min or max

    Time    O(N)
    Space   O(1)
    60 ms, faster than 66.67%
"""


class Solution:
    def countElements(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        res = 0
        for x in nums:
            if x != smallest and x != largest:
                res += 1
        return res
