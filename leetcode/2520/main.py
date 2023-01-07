"""
    1st: string

    Time    O(D)    D: the number of digits
    Space   O(1)
"""


class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        res = 0
        for c in s:
            if num % int(c) == 0:
                res += 1
        return res
