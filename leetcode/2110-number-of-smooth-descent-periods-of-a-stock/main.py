"""
    1st: math
    - for a sequence e.g. [9, 8, 7, 6]
                result =  +1 +2 +3 +4

    Time    O(N)
    Space   O(1)
    1008 ms, faster than 40.00%
"""


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 1
        desc = 1
        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                desc += 1
            else:
                desc = 1
            res += desc
        return res
