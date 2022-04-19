"""
    Time    O(N)
    Space   O(1)
"""


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = 2**32
        for x in nums:
            if abs(x) < abs(res):
                res = x
            elif abs(x) == abs(res) and x > 0:
                res = x
        return res
