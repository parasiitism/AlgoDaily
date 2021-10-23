from collections import *

"""
    1st: recursion
    - on top of subset

    Time    O(2^N)
    Space   O(2^N)
    868 ms, faster than 100.00%
"""


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.ht = Counter()
        self.dfs(nums, 0)
        maxBitOr = 0
        for k in self.ht:
            maxBitOr = max(maxBitOr, k)
        return self.ht[maxBitOr]

    def dfs(self, nums, bitOR):
        self.ht[bitOR] += 1
        for i in range(len(nums)):
            self.dfs(nums[i+1:], bitOR | nums[i])
