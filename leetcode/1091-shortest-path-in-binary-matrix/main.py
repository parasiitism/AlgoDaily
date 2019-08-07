"""
    1st approach: BFS + hashset
    - on each cell, BFS to traverse in 9 directions
    - use a hashset to avoid redundant visit

    Time    O(n^2)
    Space   O(n)
    1000 ms, faster than 14.14%
"""


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0 or grid[0][0] == 1:
            return -1
        seen = set()
        q = []
        q.append((0, 0, 1))
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if i+1 == len(grid) and j+1 == len(grid[0]) and grid[i][j] == 0:
                return steps

            directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                          (1, 0), (1, -1), (0, -1), (-1, -1)]
            for di, dj in directions:
                x = i + di
                y = j + dj
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 0:
                    q.append((x, y, steps+1))

        return -1
