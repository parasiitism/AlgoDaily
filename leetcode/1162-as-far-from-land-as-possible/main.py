"""
    1st: BFS + hashtable

    Time    O(RC^2) at max, it depends on the number of 1s
    Space   O(RC)
    2848 ms beats 5%
"""


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dm = []  # distances map
        # create an array to save the distances
        for i in range(len(grid)):
            dm.append(len(grid[0]) * [-1])
        # BFS on each cell of 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dm)
        # find the farthest cell
        res = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res = max(res, dm[i][j])
        return res

    def bfs(self, grid, x, y, dm):
        q = [(x, y, 0)]
        hs = set()
        while len(q) > 0:
            i, j, step = q.pop(0)
            # put each cell in hashset
            hs.add((i, j))
            # if the step >= distanceMap[i][j],
            # skip traversing from this cell because we cant reach the cells from here with less steps any more
            if step >= dm[i][j] and dm[i][j] != -1:
                continue
            dm[i][j] = step
            # traverse the adjcent cells
            if i-1 >= 0:
                if not (i-1, j) in hs and grid[i-1][j] == 0:
                    q.append((i-1, j, step+1))
            if i+1 < len(grid):
                if not (i+1, j) in hs and grid[i+1][j] == 0:
                    q.append((i+1, j, step+1))
            if j-1 >= 0:
                if not (i, j-1) in hs and grid[i][j-1] == 0:
                    q.append((i, j-1, step+1))
            if j+1 < len(grid[0]):
                if not (i, j+1) in hs and grid[i][j+1] == 0:
                    q.append((i, j+1, step+1))
