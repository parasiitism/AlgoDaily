def treasureIsland(grid):
    hs = set()
    q = [(0, 0, 0)]
    while len(q) > 0:
        i, j, steps = q.pop(0)
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            continue
        if (i, j) in hs:
            continue
        hs.add((i, j))
        if grid[i][j] == 'X':
            return steps
        if grid[i][j] == 'O':
            q.append((i-1, j, steps+1))
            q.append((i+1, j, steps+1))
            q.append((i, j-1, steps+1))
            q.append((i, j+1, steps+1))
    return -1


a = [
    ["O", "O", "O", "O"],
    ["D", "O", "D", "O"],
    ["O", "O", "O", "O"],
    ["X", "D", "D", "O"],
]
print(treasureIsland(a))
