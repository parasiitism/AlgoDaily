"""
    1st: BFS to count the biggest sum amongst islands

    Time    O(RC)
    Space   O(RC)
"""


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        seen = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] > 0 and (i, j) not in seen:
                    fish = self.bfs(grid, i, j, seen)
                    res = max(res, fish)
        return res

    def bfs(self, grid, x, y, seen):
        R, C = len(grid), len(grid[0])
        total = 0
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if grid[i][j] <= 0:
                continue
            key = (i, j)
            if key in seen:
                continue
            seen.add(key)
            total += grid[i][j]
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return total
