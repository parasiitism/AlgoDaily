"""
    1st: array
    - iterate from the back until non-zero digit, and then return prefix

    Time    O(N)
    Space   O(N) the result
"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = len(num)
        j = n
        for i in range(n-1, -1, -1):
            if num[i] == '0':
                j -= 1
            else:
                break
        return num[:j]
