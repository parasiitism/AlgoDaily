from functools import lru_cache

"""
    dynamic programming: DFS + hashtable

    Time    O(RC)
    Space   O(RC)
    2390 ms, faster than 95.21%
"""


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        mod = 10**9+7

        @lru_cache(None)
        def dfs(i, j):
            temp = 1
            for di, dj in dirs:
                if 0 <= i+di < R and 0 <= j+dj < C and grid[i+di][j+dj] > grid[i][j]:
                    temp += dfs(i+di, j+dj)
                    temp %= mod
            return temp

        res = 0
        for i in range(R):
            for j in range(C):
                res += dfs(i, j)
                res %= mod

        return res
