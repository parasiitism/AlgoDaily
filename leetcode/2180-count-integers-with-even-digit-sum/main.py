"""
    1st: math

    Time    O(NlogN)
    Space   O(1)
    46 ms, faster than 100.00%
"""


class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num+1):
            x = i
            d = 0
            while x > 0:
                d += x % 10
                x //= 10
            if d % 2 == 0:
                res += 1
        return res
