"""
    1st approach: math

    1. n * i = blocks + (n-1) * ans
    2. min + ans = i

    ans = blocks - n * min

    Time    O(n)
    Space   O(1)
    216 ms, faster than 79.07% 
"""


class Solution(object):
    def minMoves(self, nums):
        # n * i = blocks + (n-1) * ans
        # min + ans = i
        return sum(nums) - len(nums) * min(nums)
