"""
    linesweep in 2D
    - preprocessing with (+1),(-1)
    - prefex sum in 2D
    
    Time    O(RC+RC)
    Space   O(RC)
"""


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        linesweep2d = [[0] * (n+1) for _ in range(n+1)]
        for r1, c1, r2, c2 in queries:
            for i in range(r1, r2+1):
                linesweep2d[i][c1] += 1
                linesweep2d[i][c2+1] -= 1
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            pfs = 0
            for j in range(n):
                pfs += linesweep2d[i][j]
                res[i][j] = pfs
        return res
