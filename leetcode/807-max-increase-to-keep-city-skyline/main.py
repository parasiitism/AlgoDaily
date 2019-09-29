import sys

"""
    1st: min-max
    - on each row, find the max
    - on each column, find the max
    - traverse the whole matrix and get the grids' value by finding the minimum amongst rows_max[i] and cols_max[j]

    Time    O(RC)
    Space   O(R+C)
    52 ms, faster than 91.04%
"""


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows_max = []
        cols_max = []
        for i in range(len(grid)):
            rows_max.append(max(grid[i]))
        for j in range(len(grid[0])):
            maxV = -sys.maxsize
            for i in range(len(grid)):
                maxV = max(maxV, grid[i][j])
            cols_max.append(maxV)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rows_max[i], cols_max[j]) - grid[i][j]
        return res
