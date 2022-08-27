"""
    line sweep

    Time    O(N)
    Space   O(N)
    2616 ms, faster than 40.00%
"""


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        line_sweep = (n+1)*[0]
        for l, r, d in shifts:
            d = 1 if d == 1 else -1
            line_sweep[l] += d
            line_sweep[r+1] -= d
        pfs = 0
        res = ''
        for i in range(n):
            c = s[i]
            pfs += line_sweep[i]
            _c = chr((ord(c) - 97 + pfs) % 26 + 97)
            res += _c
        return res
