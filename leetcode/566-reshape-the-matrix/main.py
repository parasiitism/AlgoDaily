"""
    1st approach: array iterator

    Time    O(RC)
    Space   O(RC)
    100 ms, faster than 13.26%
"""


class Solution(object):
    def matrixReshape(self, matrix, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        total = len(matrix) * len(matrix[0])
        if total != r * c:
            return matrix
        res = []
        for _ in range(r):
            res.append(c * [0])
        q = Queue(matrix)
        for i in range(r):
            for j in range(c):
                res[i][j] = q.getNext()
        return res


class Queue(object):
    def __init__(self, arr):
        self.arr = arr

    def getNext(self):
        if len(self.arr) == 0:
            return None
        if isinstance(self.arr[0], list):
            self.arr = self.arr[0] + self.arr[1:]
        return self.arr.pop(0)
