from math import *

"""
    BFS + binary search
    - find the min time to get burnt for each cell by doing a mulit-sources BFS
    - upper-bound binary search
        - the min time for the person will be unable to escape
        - corner case: Both of the person and the fire reach to the destination at the same time <- should return True
            [[0,2,0,0,1],
            [0,2,0,2,2],
            [0,2,0,0,0],
            [0,0,2,2,0],
            [0,0,0,0,0]]
    
    Time    O(RClogN)
    Space   O(RC)
    1474 ms, faster than 70.00%
"""


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # min time to get burnt for each cell
        caches = [C * [2**32] for _ in range(R)]

        # mulit-sources BFS
        q = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    q.append([i, j, 0])
                elif grid[i][j] == 2:
                    grid[i][j] = -2
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i == -1 or i == R or j == -1 or j == C:
                continue
            if grid[i][j] == -2:
                continue
            if steps >= caches[i][j]:
                continue
            caches[i][j] = steps
            q.append([i-1, j, steps+1])
            q.append([i+1, j, steps+1])
            q.append([i, j-1, steps+1])
            q.append([i, j+1, steps+1])

        # binary search
        left = 0
        right = 2**32
        while left < right:
            mid = (left + right) // 2
            b = self.canReach(R, C, grid, caches, mid)
            if b:
                left = mid + 1
            else:
                right = mid
        if right > R*C:
            return 10**9
        return right - 1

    def canReach(self, R, C, grid, caches, mid):
        seen = set()
        q = [(0, 0, 0)]
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i == -1 or i == R or j == -1 or j == C:
                continue
            if grid[i][j] == -2:
                continue
            if caches[i][j] - steps < mid:
                continue
            elif caches[i][j] - steps == mid:
                # annoying corner case
                if i == R-1 and j == C-1:
                    return True
                continue
            if i == R-1 and j == C-1:
                return True
            if (i, j) in seen:
                continue
            seen.add((i, j))
            q.append((i-1, j, steps+1))
            q.append((i+1, j, steps+1))
            q.append((i, j-1, steps+1))
            q.append((i, j+1, steps+1))
        return False
