"""
    1st: sort
    
    Time    O(N)
    Space   O(N)
    96 ms, faster than 68.00%
"""


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        t = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
            t.append((count, i))
        t.sort()
        return [x[1] for x in t[:k]]
