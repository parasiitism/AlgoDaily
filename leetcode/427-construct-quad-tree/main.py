"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

"""
    1st approach: recursion
    1. check if the cells are all zeros or all ones
    2. if yes, return this grid as a leaf
    3. if no, split the grid into 4 grids and do 1) and 2) recursively

    Time    O(n^2logn)
    Space   O(n^2)
    128 ms, faster than 86.67% 
"""


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid:
            return None

        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)

        N = len(grid)

        return Node('*', False,
                    self.construct([rows[:N//2] for rows in grid[:N//2]]),
                    self.construct([rows[N//2:] for rows in grid[:N//2]]),
                    self.construct([rows[:N//2] for rows in grid[N//2:]]),
                    self.construct([rows[N//2:] for rows in grid[N//2:]]))

    def isLeaf(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return True

        areAllZeros = True
        areAllOnes = True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    areAllOnes = False
                else:
                    areAllZeros = False

        return areAllZeros or areAllOnes
