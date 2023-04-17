from heapq import *
from bisect import *

"""
    1st: brute force

    Time    O(Q*RC)
    Space   O(RC)
    LTE     17 / 21 testcases passed
"""


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for k in queries:
            cnt = self.bfs(grid, k)
            res.append(cnt)
        return res

    def bfs(self, grid, k):
        R, C = len(grid), len(grid[0])
        q = [(0, 0)]
        seen = set()
        res = 0
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if grid[i][j] >= k:
                continue
            res += 1
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return res


"""
    2nd: BFS + minheap + binary search
    
    Observation from 1st approach
    - we don't need to do BFS for every query, just use a minheap instead of a queue to keep traverse the grid,
    and then keep track of the current max along the way
    - to then use a binary search to find the res for every query

    e.g.
    [[1,2,3],
     [2,5,7],
     [3,5,1]]
    
    to compute
    path    [1, 2, 2, 3, 3, 5, 5, 1, 7]
    cur_max [1, 2, 2, 3, 3, 5, 5, 5, 7]

    queries:
    5   [1, 2, 2, 3, 3, 5, 5, 5, 7]
                        ^
    6   [1, 2, 2, 3, 3, 5, 5, 5, 7]
                                 ^
    2   [1, 2, 2, 3, 3, 5, 5, 5, 7]
            ^
    
    Time    O(RClogRC + QlogRC)
    Space   O(RC)
"""


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        R, C = len(grid), len(grid[0])
        minheap = [(grid[0][0], 0, 0)]
        seen = set()
        seen.add((0, 0))
        path = []
        while len(minheap) > 0:
            val, i, j = heappop(minheap)
            path.append((val, i, j))

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _i = i+di
                _j = j+dj
                if _i < 0 or _i == R or _j < 0 or _j == C:
                    continue
                if (_i, _j) in seen:
                    continue
                seen.add((_i, _j))

                _val = grid[_i][_j]
                heappush(minheap, (_val, _i, _j))

        path_max = []
        cur_max = 0
        for i in range(len(path)):
            cur_max = max(cur_max, path[i][0])
            path_max.append(cur_max)

        res = []
        for q in queries:
            j = bisect_left(path_max, q)
            res.append(j)

        return res
