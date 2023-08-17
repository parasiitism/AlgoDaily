from collections import *

"""
    1st: BFS + hashtable
    - record the size of every island
    - try all the coordinats on islands' border
    - use a hashtable to store the relation of (coordinate : [islandID1, islandID2, ...] 
    - then for every border coordinats, sum up the areas of its connected islands

    Time    O(RC * (2R+2C))
    Space   O(RC)
    112 ms, faster than 68.59%
"""


class Solution(object):
    def largestIsland(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        R, C = len(grid), len(grid[0])
        seen = set()
        areas = []
        boarderIslandMap = defaultdict(list)
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (i, j) not in seen:
                    area, boarderCells = self.bfs(grid, i, j, seen)

                    islandIdx = len(areas)
                    areas.append(area)

                    for x, y in boarderCells:
                        boarderIslandMap[(x, y)].append(islandIdx)

        # corner case: all cells are filled
        if len(boarderIslandMap) == 0 and len(seen) > 0:
            return R * C

        # find the max area
        res = 1
        for key in boarderIslandMap:
            area = 1
            for islandIdx in boarderIslandMap[key]:
                area += areas[islandIdx]
            res = max(res, area)
        return res

    def bfs(self, grid, x, y, seen):
        area = 0
        q = [(x, y)]
        boarderCells = set()
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if grid[i][j] == 0:
                boarderCells.add((i, j))
                continue
            if (i, j) in seen:
                continue
            seen.add((i, j))
            area += 1
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return area, boarderCells


s = Solution()

a = [[1, 0], [0, 1]]
print(s.largestIsland(a))

a = [[1, 1], [1, 0]]
print(s.largestIsland(a))

a = [[1, 1], [1, 1]]
print(s.largestIsland(a))

a = [[0, 0], [0, 0]]
print(s.largestIsland(a))

a = [[0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0]]
print(s.largestIsland(a))

print("-----")

"""
    2nd: similar to 1st
    - dont need to store the boundary zeros, only need to try all the zeros which connected to islands

    Time    O(RC * (2R+2C))
    Space   O(RC)
    120 ms, faster than 90.55%
"""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        seen = {}
        lslands_size = {}
        res = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0 or (i, j) in seen:
                    continue
                island_id = len(lslands_size)
                size = self.bfs(grid, i, j, seen, island_id)
                lslands_size[island_id] = size
                res = max(res, size)
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    connected_ids = set()
                    area = 1
                    for r, c in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                        if r < 0 or r >= R or c < 0 or c >= C:
                            continue
                        key = (r, c)
                        if key not in seen:
                            continue
                        island_id = seen[(r, c)]
                        if island_id in connected_ids:
                            continue
                        connected_ids.add(island_id)
                        area += lslands_size[island_id]

                    res = max(res, area)
        return res

    def bfs(self, grid, x, y, seen, island_id):
        R, C = len(grid), len(grid[0])
        q = deque()
        q.append([x, y])
        res = 0
        while len(q) > 0:
            i, j = q.popleft()
            if i < 0 or i >= R or j < 0 or j >= C:
                continue
            if grid[i][j] == 1:
                key = (i, j)
                if key in seen:
                    continue
                res += 1
                seen[key] = island_id
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))
        return res
