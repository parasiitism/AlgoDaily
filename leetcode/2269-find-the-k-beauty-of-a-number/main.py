"""
    1st: string

    Time    O(N)
    Space   O(1)
    78 ms, faster than 25.00%
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        res = 0
        for i in range(n - k + 1):
            sub = s[i:i+k]
            x = int(sub)
            if x == 0:
                continue
            if num % x == 0:
                res += 1
        return res
