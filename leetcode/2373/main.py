"""
    brute force

    Time    O(N^2)
    Space   O(N^2)
    271 ms, faster than 75.00%
"""


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        for i in range(n-2):
            row = []
            for j in range(n-2):
                temp = []
                for ii in range(i, i+3):
                    for jj in range(j, j+3):
                        temp.append(grid[ii][jj])
                row.append(max(temp))
            res.append(row)
        return res
