"""
    1st: hashset

    Time    O(N)
    Space   O(N)
    116 ms, faster than 50.00%
"""


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        hs = set(nums)
        while original in hs:
            original *= 2
        return original
