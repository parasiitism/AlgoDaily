"""
    1st approach: recursive dfs

    Time    O(2n)
    Space   O(n) hashtable
    416 ms, faster than 7.72%
"""


class Solution(object):
    def solve(self, grid):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # seen 2d array
        seen = []
        for i in range(len(grid)):
            seen.append(len(grid[0])*[False])
        # for each island, find out if they should be captured
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] == False and grid[i][j] == 'O':
                    touchBound = self.dfs(grid, i, j, seen)
                    if touchBound == False:
                        self.markCapture(grid, i, j)

    def dfs(self, grid, i, j, seen):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return True
        if seen[i][j] == True:
            return False
        seen[i][j] = True
        if grid[i][j] == 'O':
            up = self.dfs(grid, i-1, j, seen)
            down = self.dfs(grid, i+1, j, seen)
            left = self.dfs(grid, i, j-1, seen)
            right = self.dfs(grid, i, j+1, seen)
            return up or down or left or right
        return False

    def markCapture(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'X':
            return
        if grid[i][j] == 'O':
            grid[i][j] = 'X'
            self.markCapture(grid, i-1, j)
            self.markCapture(grid, i+1, j)
            self.markCapture(grid, i, j-1)
            self.markCapture(grid, i, j+1)


a = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
Solution().solve(a)
print(a)

a = [
    ["X", "X", "X", "O"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
Solution().solve(a)
print(a)

a = [
    ["X", "X", "X", "X", "X"],
    ["X", "O", "O", "O", "X"],
    ["X", "X", "X", "O", "X"],
    ["X", "O", "X", "O", "O"],
    ["X", "X", "X", "X", "X"],
]
Solution().solve(a)
print(a)
