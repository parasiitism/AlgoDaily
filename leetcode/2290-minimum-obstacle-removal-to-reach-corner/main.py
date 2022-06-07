from heapq import *

"""
    Dijkstra's
`
    Time    O(NlogN)
    Space   O(N)
    9737 ms, faster than 33.33%
"""


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        pq = [(0, 0, 0)]  # cost, i, j
        best = {}
        while len(pq) > 0:
            obstacles, i, j = heappop(pq)

            # The below condition will slow down the runtime
            # if i < 0 or i == R or j < 0 or j == C:
            #     continue

            obstacles += grid[i][j]  # 0 or 1

            key = (i, j)
            if key in best and obstacles >= best[key]:
                continue
            best[key] = obstacles

            # redundant conditions just for speeding up the runtime
            if i-1 >= 0:
                heappush(pq, (obstacles, i-1, j))
            if i+1 < R:
                heappush(pq, (obstacles, i+1, j))
            if j-1 >= 0:
                heappush(pq, (obstacles, i, j-1))
            if j+1 < C:
                heappush(pq, (obstacles, i, j+1))

        return best[(R-1, C-1)]
