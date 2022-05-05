"""
    string

    Time    O(N^2)
    Space   O(N)
    52 ms, faster than 35.71%
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        res = 0
        for i in range(n):
            if number[i] == digit:
                x = int(number[:i] + number[i+1:])
                res = max(res, x)
        return str(res)
