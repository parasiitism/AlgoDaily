"""
    1st: bit-wise

    Observation, when we have
    (a1 * b1) + (a1 * b2) + (a2 * b1) + (a2 * b1) = (a1 + a2) * (b1 + b2)

    Similar concept also applies for AND with XOR
    (a1 & b1) ^ (a1 & b2) ^ (a2 & b1) ^ (a2 & b2) = (a1 ^ a2) & (b1 ^ b2)

    Time    O(A+B)
    Space   O(1)
    888 ms, faster than 85.13%
"""


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xora = 0
        xorb = 0
        for a in arr1:
            xora ^= a
        for b in arr2:
            xorb ^= b
        return xora & xorb
