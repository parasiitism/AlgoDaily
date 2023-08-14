"""
    1st: brute-force

    Time    O(N^2)
    Space   O(N)
"""


from collections import *


class Solution:
    def finalString(self, s: str) -> str:
        chars = []
        for c in s:
            if c == 'i':
                chars.reverse()
            else:
                chars.append(c)
        return ''.join(chars)


"""
    2nd: double-ended queue

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def finalString(self, s: str) -> str:
        dq = deque()
        flip = False
        for c in s:
            if c == 'i':
                flip = not flip
            else:
                if flip:
                    dq.appendleft(c)
                else:
                    dq.append(c)
        if flip:
            return ''.join(list(dq)[::-1])
        return ''.join(list(dq))
