"""
    1st: array
    - find 2 smallest numbers from an array without using sorting

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest1 = 2**32
        smallest2 = 2**32
        for p in prices:
            if p < smallest1:
                smallest2 = smallest1
                smallest1 = p
            elif p < smallest2:
                smallest2 = p
        leftover = money - smallest1 - smallest2
        if leftover < 0:
            return money
        return leftover
