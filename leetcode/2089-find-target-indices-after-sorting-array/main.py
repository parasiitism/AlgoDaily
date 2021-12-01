from bisect import *

"""
    1st: sort + binary search
    Time    O(NlogN + 2logN + N)
    Space   O(N)
    40 ms, faster than 100.00%
"""


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        s_nums = sorted(nums)
        left = bisect_left(s_nums, target)
        right = bisect_right(s_nums, target)
        return [i for i in range(left, right)]
