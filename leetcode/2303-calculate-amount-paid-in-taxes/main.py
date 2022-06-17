"""
    math

    Time    O(N)
    Space   O(1)
    127 ms, faster than 15.38%
"""


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        for i in range(len(brackets)):
            upper, percent = brackets[i]
            if i == 0:
                tax = min(upper, income) * percent / 100.0
                taxes += max(tax, 0)
            else:
                tax = (min(upper, income) - brackets[i-1][0]) * percent / 100.0
                taxes += max(tax, 0)
        return taxes
