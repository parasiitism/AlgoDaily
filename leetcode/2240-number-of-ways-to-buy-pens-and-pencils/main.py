"""
    1st: math

    Time    O(N)
    Space   O(1)
    975 ms, faster than 100.00%
"""


class Solution:
    def waysToBuyPensPencils(self, total: int, pen: int, pensil: int) -> int:
        res = 0
        i = 0
        while i * pen <= total:
            r = total - i * pen
            j = r // pensil + 1
            res += j
            i += 1
        return res
