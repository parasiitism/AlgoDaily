"""
    1st: bipartite

    Time    O(RC)
    Space   O(RC)
    2265 ms, faster than 100.00%
"""


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        seen = set()

        def dfs(i, j, color):

            blackWhite = [0, 0]
            if i < 0 or i == R or j < 0 or j == C:
                return blackWhite

            if grid[i][j] == 0:
                return blackWhite

            key = (i, j)
            if key in seen:
                return blackWhite
            seen.add(key)

            blackWhite[color] += 1
            for di, dj in dirs:
                _i = i + di
                _j = j + dj
                r = dfs(_i, _j, (color+1) % 2)  # bipartite
                blackWhite[0] += r[0]
                blackWhite[1] += r[1]
            return blackWhite

        res = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    continue
                if (i, j) in seen:
                    continue
                res += min(dfs(i, j, 0))
        return res
