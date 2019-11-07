"""
    1st: BFS + hashtable
    - paint the island
    - unpaint the cells that not on the border

    remarks:
    - we can do the same thing with DFS to paint the island

    Time    O(RC + 2K) k: number of connected cells depends on input
    Space   O(RC)
    112 ms, faster than 85.42% 
"""


class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        origColor = None
        isPainted = False
        painted = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == r0 and j == c0 and isPainted == False:
                    origColor = grid[i][j]
                    self.paint(grid, i, j, origColor, color, painted)
                    isPainted = True
        cands = self.findCandidatesToPaintBack(grid, painted, origColor)
        for i, j in cands:
            grid[i][j] = origColor
        return grid

    def paint(self, grid, x, y, origColor, color, painted):
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                continue
            if grid[i][j] == origColor:
                if (i, j) in painted:
                    continue
                painted.add((i, j))
                grid[i][j] = color
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))

    def findCandidatesToPaintBack(self, grid, painted, origColor):
        candidates = []
        for i, j in painted:
            s = set()
            s.add(1)
            if i-1 >= 0 and (i-1, j) in painted:
                s.add(1)
            else:
                s.add(-1)

            if i+1 < len(grid) and (i+1, j) in painted:
                s.add(1)
            else:
                s.add(-1)

            if j-1 >= 0 and (i, j-1) in painted:
                s.add(1)
            else:
                s.add(-1)

            if j+1 < len(grid[0]) and (i, j+1) in painted:
                s.add(1)
            else:
                s.add(-1)

            if len(s) == 1:
                candidates.append((i, j))
        return candidates
