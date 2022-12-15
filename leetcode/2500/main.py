"""
    1. sort the rows
    2. accumulate the max value by col

    Time    O(R * ClogC + RC)
    Space   O(1)
"""


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        for row in grid:
            row.sort()
        res = 0
        for j in range(C):
            col_max = 0
            for i in range(R):
                col_max = max(col_max, grid[i][j])
            res += col_max
        return res
