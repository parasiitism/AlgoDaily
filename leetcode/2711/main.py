"""
    1st: 2D array
    - just implement it

    Time    O(RC * min(R, C))
    Space   O(RC)
"""


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        res = [C * [0] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                topLeft = set()
                bottomRight = set()
                _i, _j = i, j
                while _i-1 >= 0 and _j-1 >= 0:
                    _i -= 1
                    _j -= 1
                    topLeft.add(grid[_i][_j])
                _i, _j = i, j
                while _i+1 < R and _j+1 < C:
                    _i += 1
                    _j += 1
                    bottomRight.add(grid[_i][_j])
                res[i][j] = abs(len(topLeft) - len(bottomRight))
        return res
