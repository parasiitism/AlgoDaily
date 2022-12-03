"""
    array

    Time    O(RC)
    Space   O(RC)
    4358 ms, faster than 43.73%
"""


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        onesRows = R * [0]
        onesCols = C * [0]
        zerosRows = R * [0]
        zerosCols = C * [0]
        for i in range(R):
            ones = 0
            for j in range(C):
                ones += grid[i][j]
            onesRows[i] = ones
            zerosRows[i] = C - ones
        for j in range(C):
            ones = 0
            for i in range(R):
                ones += grid[i][j]
            onesCols[j] = ones
            zerosCols[j] = R - ones

        res = []
        for i in range(R):
            temp = []
            for j in range(C):
                temp.append(onesRows[i] + onesCols[j] -
                            zerosRows[i] - zerosCols[j])
            res.append(temp)
        return res
