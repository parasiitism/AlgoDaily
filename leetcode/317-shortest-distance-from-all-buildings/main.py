import sys

"""
    1st approach: BFS + hastable
    - similar to lc286: walls and gates
    - on each cell
        - sum up all the steps from each buildings
        - record the number of buildings which can access this cell
    - find the min

    Time    O(kRRCC) k: number of buildings
    Space   O(2RC)
    1048 ms, faster than 14.66% 
"""


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        # distance from buildings
        dist = []
        for _ in range(len(grid)):
            dist.append(len(grid[0]) * [0])
        # no of buildings
        visitCounts = []
        for _ in range(len(grid)):
            visitCounts.append(len(grid[0]) * [0])
        buildingCount = 0
        # reverse the graph
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # bfs
                    buildingCount += 1
                    self.bfs(grid, i, j, dist, visitCounts)
        # get the min distance from the cells as long as each cell has been visited by all buildings
        res = sys.maxsize
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and visitCounts[i][j] == buildingCount:
                    res = min(res, dist[i][j])
        if res == sys.maxsize:
            return -1
        return res

    def bfs(self, grid, x, y, dist, visitCounts):
        q = [(x, y, 0)]
        seen = set()
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if (i == x and j == y) or (grid[i][j] != 1 and grid[i][j] != 2):
                dist[i][j] += steps
                visitCounts[i][j] += 1
                if i-1 >= 0:
                    q.append((i-1, j, steps + 1))
                if i+1 < len(grid):
                    q.append((i+1, j, steps + 1))
                if j-1 >= 0:
                    q.append((i, j-1, steps + 1))
                if j+1 < len(grid[0]):
                    q.append((i, j+1, steps + 1))


a = [
    [1, 0, 2, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
print(Solution().shortestDistance(a))

a = [
    [0, 2, 1],
    [1, 0, 2],
    [0, 1, 0],
]
print(Solution().shortestDistance(a))
