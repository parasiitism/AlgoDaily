"""
    hashtable

    Time    O(RC)
    Space   O(RC)
    715 ms, faster than 100.00%
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N = len(grid)
        rowCtr = Counter()
        for i in range(N):
            key = tuple(grid[i])
            rowCtr[key] += 1
        res = 0
        for j in range(N):
            cols = []
            for i in range(N):
                cols.append(grid[i][j])
            key = tuple(cols)
            if key in rowCtr:
                res += rowCtr[key]
        return res
