"""
    bit-op observation
    - https://leetcode.com/problems/find-xor-beauty-of-array/solutions/3015014/why-just-xor-of-all-numbers-works/?orderBy=most_votes
    - i hate bit-op

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res
