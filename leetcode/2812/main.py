from collections import *

"""
    1st: binary search + BFS
    - build a 2D array in which represent the closest distance to a thieve on every cell, like rotten tomatos
    - do a upper-bound binary search to find out the path where all the cells are at least MID steps from their thieve

    Time    O(RC + RClogR)
    Spce    O(RC)
"""


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dists = self.distsFromThieves(grid)
        left = 0
        right = 400
        while left < right:
            mid = (left + right) // 2
            b = self.canTraverse(dists, mid)
            if b == False:
                right = mid
            else:
                left = mid + 1

        return left - 1

    def canTraverse(self, dists, atLeast):
        R, C = len(dists), len(dists[0])
        q = deque()
        q.append((0, 0))
        seen = set()
        while len(q) > 0:
            i, j = q.popleft()
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if dists[i][j] < atLeast:
                continue
            if i == R-1 and j == C-1:
                return True
            key = (i, j)
            if key in seen:
                continue
            seen.add(key)
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return False

    def distsFromThieves(self, grid):
        R, C = len(grid), len(grid[0])
        q = deque()
        dists = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
            dists.append(C * [2**32])
        while len(q) > 0:
            i, j, steps = q.popleft()
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if steps >= dists[i][j]:
                continue
            dists[i][j] = steps
            q.append((i-1, j, steps+1))
            q.append((i+1, j, steps+1))
            q.append((i, j-1, steps+1))
            q.append((i, j+1, steps+1))
        return dists
