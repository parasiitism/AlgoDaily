"""
    1st: binary search + BFS
    - similar to leetcode778
    - since after certain number of cells being flooded the land cannot be crossed,
        we can do upper-bound binary search to find out the last day to cross the land
    
    Time    O(N + RClogN)
    Space   O(N) for the hashset
    4504 ms, faster than 13.32% 
"""


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        R, C = row, col
        N = len(cells)
        for i in range(N):
            x, y = cells[i]
            cells[i] = (x-1, y-1)
        left = 0
        right = N
        while left < right:
            mid = (left + right)//2
            b = self.bfs(R, C, cells, mid)
            if b:
                left = mid + 1
            else:
                right = mid
        return left - 1

    def bfs(self, R, C, cells, mid):
        seen = set()
        flooded = set(cells[:mid])
        q = [(0, j) for j in range(C)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i == R:
                return True
            if i == -1 or j == -1 or j == C:
                continue
            key = (i, j)
            if key in flooded:
                continue
            if key in seen:
                continue
            seen.add(key)
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return False
