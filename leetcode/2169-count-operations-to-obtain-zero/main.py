"""
    1st: math

    Time    O(N)
    Space   O(1)
    183 ms, faster than 25.00%
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ma = max(num1, num2)
        mi = min(num1, num2)
        res = 0
        while ma > 0 and mi > 0:
            res += 1
            ma -= mi
            if ma < mi:
                ma, mi = mi, ma
        return res
