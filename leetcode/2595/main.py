"""
    1st: bit op

    Time    O(logN base 2)
    Space   O(1)
"""


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        i = 0
        while n > 0:
            r = n % 2
            n = n//2
            if r == 1:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
            i += 1
        return [even, odd]
