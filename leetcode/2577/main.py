from heapq import *

"""
    Dijkstra
    - unless grid[0][1] > 1 and grid[1][0] > 1, otherwise we must be able to reach the right-bottom
    - the way to do it is we wait by playing 'ping pong' between 2 adjacent cells, the wait-time to reach the adjacent cell must be 1, 3, 5, 7, 9...etc


    Time    O(RClogRC)
    Space   O(RC)
"""
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        R, C = len(grid), len(grid[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        pq = [(0, 0, 0)] # time, i, j
        seen = set()
        while len(pq) > 0:
            steps, i, j = heappop(pq)
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if i == R-1 and j == C-1:
                return steps
            for di, dj in dirs:
                _i, _j = i+di, j+dj
                if _i < 0 or _i > R-1 or _j < 0 or _j > C-1:
                    continue
                wait = 0
                if (grid[_i][_j] - steps) % 2 == 0:
                    wait = 1
                heappush(pq, (max(steps + 1, grid[_i][_j] + wait), _i, _j))
        return -1