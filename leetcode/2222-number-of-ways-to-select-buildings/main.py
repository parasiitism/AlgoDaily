"""
    1st: dynamic programming
    - there are only 2 patterns at the end, and those patterns can be built using the 1-digit-less patterns

    Time    O(N)
    Space   O(6)
    966 ms, faster than 76.64%
"""


class Solution:
    def numberOfWays(self, s: str) -> int:
        p0, p01, p010 = 0, 0, 0
        p1, p10, p101 = 0, 0, 0
        for i in range(len(s)):
            c = int(s[i])
            if c == 0:
                p0 += 1
                p10 += p1
                p010 += p01
            else:
                p1 += 1
                p01 += p0
                p101 += p10
        return p010 + p101
