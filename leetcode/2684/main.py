"""
    graph
    - weird traversing rules but clear to implement

    Time    O(RC)
    Space   O(RC)
"""


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = []
        for i in range(R):
            q.append((i, 0, 0))
        seen = set()
        res = 0
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if (i, j) in seen:
                continue
            seen.add((i, j))
            res = max(res, steps)
            for di, dj in [(-1, 1), (0, 1), (1, 1)]:
                _i = i + di
                _j = j + dj
                if 0 <= _i < R and 0 <= _j < C and grid[i][j] < grid[_i][_j]:
                    q.append((_i, _j, steps + 1))
        return res
