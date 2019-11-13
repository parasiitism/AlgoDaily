class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [0] * n
        cols = [0] * m
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        # matrix = []
        res = 0
        for i in range(n):
            for j in range(m):
                x = rows[i] + cols[j]
                if x % 2 == 1:
                    res += 1
        return res
