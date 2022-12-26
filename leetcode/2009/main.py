from bisect import *

"""
    binary search
    - use upperbound binary search to count how many numbers are in the current sliding window
    , so we know how many numbers are missing

    e.g.
    
    Indx:        0        1  2     3            4   5       6
    question:   [1,       4, 5,    7,           11, 12,     14]
    
    idx=0       ^
                binary-search for the index of the first number > 1+7-1 = 7, in this case is 4,
                so it means currently we have 4-0 = 4 numbers in the sliding window,
                it implies that n - 4 = 7 - 4 = 3 numbers are missing in the sliding window
    
    idx=1                 ^
                          binary-search > 4+7-1 = 10, result = 4, so we have 4-1 = 3 numbers in the sliding window,
                          implying that n = 3 = 4 numbers are missing in the sliding window
    ...

    Time    O(NlogN)
    Space   O(N)
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(set(nums))
        res = 2**32
        for i in range(len(sorted_nums)):
            x = sorted_nums[i]
            j = bisect_right(sorted_nums, x + n - 1)
            res = min(res, n - (j - i))
        return res
