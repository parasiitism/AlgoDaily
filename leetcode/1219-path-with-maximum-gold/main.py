from typing import List

"""
    1st: backtracking
    - recursively traverse the matrix with dfs
    - to avoid redundant visiting:
        1. temporary put the candidate into the hashtable
        2. remove the candidate after the exploration
        This technique is known as backtacking
    - similar to lc51, 52

    Time    O(RRCC)
    Space   O(RC)
    1724 ms, faster than 41.22%
"""


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                hs = set()
                hs.add((i, j))
                self.dfs(grid, i, j, hs, grid[i][j])
        return self.res

    def dfs(self, grid: List[List[int]], i: int, j: int, hs: set, total: int) -> None:
        self.res = max(self.res, total)
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for di, dj in dirs:
            x = i + di
            y = j + dj
            if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]):
                continue
            if grid[x][y] == 0:
                continue

            if (x, y) in hs:
                continue
            hs.add((x, y))      # 1. put the candidate into the hashtable
            self.dfs(grid, x, y, hs, total + grid[x][y])
            hs.remove((x, y))   # 2. remove the candidate after the exploration


s = Solution()

a = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(s.getMaximumGold(a))

a = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
print(s.getMaximumGold(a))
