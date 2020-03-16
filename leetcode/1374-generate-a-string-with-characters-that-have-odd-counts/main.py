"""
    1st: ...

    Time    O(N)
    Space   O(1)
    20 ms, faster than 96.36%
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return n * 'a'
        return (n-1) * 'a' + 'b'
