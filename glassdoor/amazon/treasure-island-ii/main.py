import sys


def treasureIslandII(grid):

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    minSteps = sys.maxsize
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                steps = bfs(grid, i, j)
                minSteps = min(minSteps, steps)
    return minSteps


def bfs(grid, x, y):
    hs = set()
    q = [(x, y, 0)]
    while len(q) > 0:
        i, j, steps = q.pop(0)
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            continue
        if (i, j) in hs:
            continue
        hs.add((i, j))
        if grid[i][j] == 'X':
            return steps
        if grid[i][j] == 'O' or (i == x and j == y):
            q.append((i-1, j, steps+1))
            q.append((i+1, j, steps+1))
            q.append((i, j-1, steps+1))
            q.append((i, j+1, steps+1))
    return sys.maxsize


a = [
    ['S', 'O', 'O', 'S', 'S'],
    ['D', 'O', 'D', 'O', 'D'],
    ['O', 'O', 'O', 'O', 'X'],
    ['X', 'D', 'D', 'O', 'O'],
    ['X', 'D', 'D', 'D', 'O']
]
print(treasureIslandII(a))
