class Solution(object):

    def __init__(self):
        self.visited = {}

    def findNine(self, grid):
        return self.dfs(grid, 0, 0)

    def dfs(self, grid, i, j):
        if i < 0 or i+1 > len(grid) or j < 0 or j+1 > len(grid[0]):
            return False
        # avoid visited point
        key = str(i)+','+str(j)
        if key in self.visited:
            return False
        self.visited[key] = True

        # check if arrive 9
        if grid[i][j] == 9:
            return True
        elif grid[i][j] == 0:
            return self.dfs(grid, i-1, j) or \
                self.dfs(grid, i+1, j) or \
                self.dfs(grid, i, j-1) or \
                self.dfs(grid, i, j+1)
        return False


a = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 1, 9],
]
print(Solution().findNine(a))

a = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 9],
]
print(Solution().findNine(a))

a = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 9, 0, 0, 0, 0],
]
print(Solution().findNine(a))

a = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 9, 0, 1, 0, 0],
]
print(Solution().findNine(a))
