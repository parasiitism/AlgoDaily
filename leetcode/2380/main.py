"""
    string
    - just implement the description

    Time    O(N^2)
    Space   O(N)
    5903 ms, faster than 20.00%
"""


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        while True:
            _s = self.rearrange(s)
            if _s == s:
                break
            s = _s
            count += 1
        return count

    def rearrange(self, s):
        res = [s[0]]
        for i in range(1, len(s)):
            p = s[i-1]
            c = s[i]
            if p == '0' and c == '1':
                res.pop()
                res.append('10')
            else:
                res.append(c)
        _s = ''.join(res)
        return _s
