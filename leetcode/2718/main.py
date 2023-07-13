"""
    1st: brain teaser
    - it is too time consuming to simulate the operations
    - but the observation is
        - by processing the queries in reverse, you make sure that no further changes can be made on that row or column
        - then we can sum up the values without considering the used row/col indices
    
    Time    O(Q)
    Space   O(N)
"""


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        cols = set()
        rows = set()
        res = 0
        for t, i, v in queries[::-1]:
            if t == 0:
                if i not in rows:
                    res += (n - len(cols)) * v
                rows.add(i)
            elif t == 1:
                if i not in cols:
                    res += (n - len(rows)) * v
                cols.add(i)
        return res
