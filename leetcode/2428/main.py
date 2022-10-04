"""
    Array brute force

    Time    O(RC)
    Space   O(1)
    849 ms, faster than 20.00%
"""


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        for i in range(1, R-1):
            for j in range(1, C-1):
                res = max(res, self.hourglass(grid, i, j))
        return res

    def hourglass(self, grid, i, j):
        top = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
        bottom = grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
        return top + grid[i][j] + bottom
