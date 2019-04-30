"""
    1st approach
	- recursive dfs
	- when we see an one, dfs its neightbours to calculate its area and compare to the potential result
	- if it is larger than the potential result, set it as the potential result

	Time    O(n)
	Space   O(n) hashtable
	88ms 58.34%
"""


class Solution(object):
    def __init__(self):
        self.res = 0
        self.cur = 0

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        visited = []
        for line in grid:
            visited.append(len(line)*[False])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.cur = 0
                    self.dfs(grid, i, j, visited)
                    if self.cur > self.res:
                        self.res = self.cur
                    self.cur = 0
                else:
                    visited[i][j] = True

        return self.res

    def dfs(self, grid, i, j, visited):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            return
        if visited[i][j] == True:
            return
        visited[i][j] = True
        if grid[i][j] == 1:
            self.cur += 1
            self.dfs(grid, i-1, j, visited)
            self.dfs(grid, i+1, j, visited)
            self.dfs(grid, i, j-1, visited)
            self.dfs(grid, i, j+1, visited)


a = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(a))

a = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(a))

print("---")

"""
    2nd approach
	- iterative bfs
	- when we see an one, bfs its neightbours to calculate its area and compare to the potential result
	- if it is larger than the potential result, set it as the potential result

	Time    O(n)
	Space   O(n) hashtable
	88ms 58.34%
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        visited = []
        for line in grid:
            visited.append(len(line)*[False])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = self.bfs(grid, i, j, visited)
                    res = max(res, area)
        return res

    def bfs(self, grid, x, y, visited):
        q = []
        q.append((x, y))
        area = 0
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i+1 > len(grid) or j < 0 or j+1 > len(grid[0]):
                continue
            if visited[i][j] == True:
                continue
            visited[i][j] = True
            if grid[i][j] == 1:
                area += 1
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))
        return area


a = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(a))

a = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(a))

print("---")
