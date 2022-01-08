"""
    1st: brain teaser
    1. for every row, if the 1st item = 1, flip the row 
    2. for every col, if the 1st item = 1, flip the col
    3. if all cell = 0, return True

    Time    O(RC)
    Space   O(1)
    514 ms, faster than 100.00%
"""


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        for i in range(R):
            if grid[i][0] == 1:
                for j in range(C):
                    grid[i][j] ^= 1
        for j in range(C):
            if grid[0][j] == 1:
                for i in range(R):
                    grid[i][j] ^= 1
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return False
        return True
