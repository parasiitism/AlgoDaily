"""
    1st: string

    Time    O(N)
    Space   O(N) result
    67 ms, faster than 33.33%
"""


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        cur = ''
        for c in s:
            cur += c
            if len(cur) == k:
                res.append(cur)
                cur = ''
        if len(cur) != 0:
            diff = k - len(cur)
            cur += diff * fill
            res.append(cur)
        return res
