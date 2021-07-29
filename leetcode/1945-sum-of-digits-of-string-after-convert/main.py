"""
    1st: math

    Time    O(Nk)
    Space   O(N)
    36 ms, faster than 87.01%
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        x = ''
        for c in s:
            idx = ord(c) - ord('a') + 1
            x += str(idx)
        num = int(x)
        for i in range(k):
            _num = 0
            while num > 0:
                _num += num % 10
                num //= 10
            num = _num
        return num
