"""
    math

    Time    O(1)
    Space   O(1)
"""


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        if numOnes > 0 and k > 0:
            to_add = min(numOnes, k)
            res += to_add
            k -= to_add
        if numZeros > 0 and k > 0:
            to_add = min(numZeros, k)
            k -= to_add
        if numNegOnes > 0 and k > 0:
            to_add = min(numNegOnes, k)
            res -= to_add
            k -= to_add
        return res
