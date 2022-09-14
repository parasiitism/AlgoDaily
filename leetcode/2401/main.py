"""
    sliding window
    - the brainteaser is to use OR and XOR
    

    Time    O(N)
    Space   O(1)
    1598 ms, faster than 46.54%
"""


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = AND = j = 0
        for i in range(len(nums)):
            while AND & nums[i]:
                AND ^= nums[j]
                j += 1
            AND |= nums[i]
            res = max(res, i - j + 1)
        return res
