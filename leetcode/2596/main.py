"""
    backtracking + hashtable

    Time    O(N^2)  every cell will be visisted once
    Space   O(N^2)  the hashtable and the depth of the recursion tree
"""


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        final_step = n*n-1
        dirs = [
            (-2, 1), (-1, 2), (1, 2), (2, 1),
            (2, -1), (1, -2), (-1, -2), (-2, -1)
        ]
        seen = set()

        def backtracking(i, j, steps):
            if i < 0 or i >= n or j < 0 or j >= n:
                return False
            if grid[i][j] != steps:
                return False
            key = (i, j)
            if key in seen:
                return False
            seen.add(key)
            if grid[i][j] == final_step:
                return True
            b = False
            for di, dj in dirs:
                b = b or backtracking(i+di, j+dj, steps+1)
            if b == False:
                seen.remove(key)
            return b

        return backtracking(0, 0, 0)
