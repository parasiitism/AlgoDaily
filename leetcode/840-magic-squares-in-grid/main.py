"""
    1st approach: brute force checking
    - for every cell within (M-2, N-2), get the sums from the rows, cols and diagonals and check if they equal

    Time    O(10RC)
    Space   O(9) -> O(1)
    28 ms, faster than 58.18%
"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.isMagic(grid, i, j):
                    count += 1
        return count

    def isMagic(self, grid, x, y):
        # check unique
        hs = set()
        for i in range(x, x+3):
            for j in range(y, y+3):
                if grid[i][j] < 1 or grid[i][j] > 9:
                    return False
                hs.add(grid[i][j])
        if len(hs) != 9:
            return False
        sums = []
        # rows
        sums.append(grid[x][y] + grid[x][y+1] + grid[x][y+2])
        sums.append(grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y+2])
        sums.append(grid[x+2][y] + grid[x+2][y+1] + grid[x+2][y+2])
        # cols
        sums.append(grid[x][y] + grid[x+1][y] + grid[x+2][y])
        sums.append(grid[x][y+1] + grid[x+1][y+1] + grid[x+2][y+1])
        sums.append(grid[x][y+2] + grid[x+1][y+2] + grid[x+2][y+2])
        # diag
        sums.append(grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2])
        sums.append(grid[x][y+2] + grid[x+1][y+1] + grid[x+2][y])
        # check sums
        for i in range(1, len(sums)):
            if sums[i-1] != sums[i]:
                return False
        return True
