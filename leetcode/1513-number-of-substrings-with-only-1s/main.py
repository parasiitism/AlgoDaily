"""
    1st: math

    Time    O(N)
    Space   O(1)
    168 ms, faster than 33.33%
"""


class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        cur = 0
        for c in s:
            if c == '0':
                cur = 0
            elif c == '1':
                cur += 1
                res += cur % (10**9 + 7)
        return res % (10**9 + 7)
