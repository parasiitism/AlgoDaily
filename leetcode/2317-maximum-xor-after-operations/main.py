"""
    brain teaser
    - An operation can remove a bit, but cannot add one. So the max must be the OR

    Time    O(N)
    Space   O(1)
    721 ms, faster than 65.43%
"""


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res |= x
        return res
