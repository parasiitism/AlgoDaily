"""
    1st: BFS
    
    Time    O(RC)
    Space   O(RC)
    240 ms, faster than 9.70%
"""


class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        hs = set()
        q = [(r0, c0)]
        res = []
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            if (i, j) in hs:
                continue
            hs.add((i, j))
            res.append((i, j))
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        return res
