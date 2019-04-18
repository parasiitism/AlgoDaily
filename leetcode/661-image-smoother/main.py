"""
    1st approach: brute force

    Time    O(9n) n = row * col
    Space   O(n)
    752 ms, faster than 27.79%
"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(M) == 0 or len(M[0]) == 0:
            return []

        res = []
        for i in range(len(M)):
            res.append(len(M[0]) * [0])

        for i in range(len(M)):
            for j in range(len(M[0])):
                res[i][j] = self.countAdjacent(M, i, j)

        return res

    def countAdjacent(self, M, x, y):
        count = 0
        ones = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < len(M) and j >= 0 and j < len(M[0]):
                    count += 1
                    ones += M[i][j]
        return ones/count
