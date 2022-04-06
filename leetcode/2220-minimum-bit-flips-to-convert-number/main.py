"""
    1st: bit op

    Time    O(64+32)
    Space   O(64)
    49 ms, faster than 16.67% 
"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = self.getBin(start)
        b = self.getBin(goal)
        res = 0
        for i in range(32):
            if a[i] != b[i]:
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
