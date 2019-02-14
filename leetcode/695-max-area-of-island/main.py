class Solution(object):

    def __init__(self):
        self.res = 0
        self.cur = 0

    def maxAreaOfIsland(self, grid):
        """
        1st approach
        - recursive dfs
        - when we see an one, dfs its neightbours to calculate its area and compare to the potential result
        - if it is larger than the potential result, set it as the potential result

        i think the 2nd way is to do it with an iterative dfs

        Time    O(n)
        Space   O(n) hashtable
        88 ms, faster than 38.07% 
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        visited = []
        for line in grid:
            temp = []
            for unit in line:
                temp.append(False)
            visited.append(temp)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.cur = 0
                    self.dfs(grid, i, j, visited)
                    self.cur = 0
                else:
                    visited[i][j] = True

        return self.res

    def dfs(self, grid, i, j, visited):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or visited[i][j] == True:
            return
        visited[i][j] = True
        if grid[i][j] == 1:
            self.cur += 1
            if self.cur > self.res:
                self.res = self.cur
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
