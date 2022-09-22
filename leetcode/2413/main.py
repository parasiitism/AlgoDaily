"""
    math

    Time    O(1)
    Space   O(1)
    50 ms, faster than 27.27%
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return 2 * n
