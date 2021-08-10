"""
    1st: array

    Time    O(N)
    Space   O(N)
    584 ms, faster than 25.00%
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        cur = ''
        count = 0
        for i in range(len(s)):
            c = s[i]
            if c == cur:
                count += 1
                if count < 3:
                    res += c
            else:
                cur = c
                count = 1
                res += c
        return res
