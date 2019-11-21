"""
    1st: math
    - find the project areas by accumulating the maxHeight for each row and each column
    - dont forget to add up the projects area from z

    Time    O(2RC)
    Space   O(1)
    60 ms, faster than 64.61%
"""


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        for i in range(len(grid)):
            # from left to right
            maxHeight = 0
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    area += 1
                maxHeight = max(maxHeight, grid[i][j])
            area += maxHeight
        for j in range(len(grid[0])):
            # from top to down
            maxHeight = 0
            for i in range(len(grid)):
                maxHeight = max(maxHeight, grid[i][j])
            area += maxHeight
        return area
