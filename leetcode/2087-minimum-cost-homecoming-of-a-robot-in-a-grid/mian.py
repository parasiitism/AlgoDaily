"""
    1st: math
    - since the costs are by rows or cols, all the shortest paths have the same cost
"""


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        res = 0
        i, j = startPos
        x, y = homePos
        while i != x:
            if i < x:
                i += 1
            else:
                i -= 1
            res += rowCosts[i]
        while j != y:
            if j < y:
                j += 1
            else:
                j -= 1
            res += colCosts[j]
        return res
