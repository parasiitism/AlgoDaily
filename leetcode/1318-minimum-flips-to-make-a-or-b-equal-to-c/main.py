"""
    1st: bit op + math
    - just compare diff at every bit index

    Time    O(32*4)
    Space   O(32*3)
    38 ms, faster than 71.26%
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        A = self.getBin(a)
        B = self.getBin(b)
        C = self.getBin(c)
        res = 0
        for i in range(32):
            if A[i] | B[i] == C[i]:
                continue
            if C[i] == 0:
                if A[i] == 1:
                    res += 1
                if B[i] == 1:
                    res += 1
            else:
                res += 1
        return res

    def getBin(self, num):
        b = 32 * [0]
        i = 0
        while num > 0:
            b[i] = num % 2
            num //= 2
            i += 1
        return b
