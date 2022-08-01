"""
    hashset

    Time    O(N)
    Space   O(N)
    50 ms, faster than 50.00%
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distincts = set(nums)
        mi = min(distincts)
        n = len(distincts)
        if mi == 0:
            return n - 1
        return n
