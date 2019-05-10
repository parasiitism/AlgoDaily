"""
    1st approach: bfs 
    - need a 2D array. for each cell, calculate the distance from 2s
    - after bfs, if there is still an 1 which the distance is not calculated, return -1

    Time    O(kRC) k=number of rotten oranges in the beginning
    Space   O(RC)
    64 ms, faster than 19.36%
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        dist = []
        for _ in range(len(grid)):
            dist.append(len(grid[0]) * [sys.maxsize])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.bfs(i, j, grid, dist)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if dist[i][j] == sys.maxsize:
                        return -1
                    else:
                        res = max(res, dist[i][j])
        return res
        
    def bfs(self, x, y, grid, dist):
        
        seen = set()
        
        q = [(x, y, 0)]
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i+1 > len(grid) or j < 0 or j+1 > len(grid[0]):
                continue
            if (i == x and j == y) or grid[i][j] == 1:
                
                key = str(i) + ',' + str(j)
                if key in seen:
                    continue
                seen.add(key)
                
                dist[i][j] = min(dist[i][j], steps)
                
                q.append((i-1, j, steps+1))
                q.append((i+1, j, steps+1))
                q.append((i, j-1, steps+1))
                q.append((i, j+1, steps+1))