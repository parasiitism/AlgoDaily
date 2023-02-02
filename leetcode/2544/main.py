"""
    Array

    Time    O(D)
    Space   O(1)
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = [int(c) for c in str(n)]
        res = 0
        for i in range(len(digits)):
            if i % 2 == 0:
                res += digits[i]
            else:
                res -= digits[i]
        return res
