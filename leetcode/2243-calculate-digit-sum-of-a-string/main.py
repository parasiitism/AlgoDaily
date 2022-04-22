"""
    1st: string

    Time    O(N)
    Space   O(N)
    35 ms, faster than 70.19% 
"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            subs = []
            buf = ''
            x = 0
            for c in s:
                buf += c
                x += int(c)
                if len(buf) == k:
                    subs.append(str(x))
                    buf = ''
                    x = 0
            if len(buf) > 0:
                subs.append(str(x))
                buf = ''
                x = 0
            s = ''.join(subs)
        return s
