import sys

"""
    Given a matrix, return the sum of the maximum submatrix
    e.g.
    [
      [6, -5,  -7,  4, -4],
      [-9,  3,  -6,  5,  2],
      [-10,  4,   7, -6,  3],
      [-8,  9,  -3,  3, -7],
    ]
    return 17
    because
    [
      [4, 7],
      [9, -3],
    ] is the maximum submatrix and all numbers within it sum up to 17

    ref:
    - https://www.youtube.com/watch?v=-FgseNO-6Gk

    Time    O(c^2*r)
    Space   O(r)
"""


class Solution(object):

    def maxSumRetangle(self, matrix):
        left, right = 0, 0
        res = -sys.maxsize
        # isExpanding = True
        for i in range(len(matrix[0])):
            window = len(matrix) * [0]
            for j in range(i, len(matrix[0])):
                # compute values in window
                for k in range(len(window)):
                    window[k] += matrix[k][j]
                # compare
                temp = self.kadan(window)
                res = max(res, temp)
        return res

    def kadan(self, nums):
        res = -sys.maxsize
        cur = -sys.maxsize
        for num in nums:
            cur = max(cur+num, num)
            res = max(res, cur)
        return res


a = [
    [6, -5,  -7,  4, -4],
    [-9,  3,  -6,  5,  2],
    [-10,  4,   7, -6,  3],
    [-8,  9,  -3,  3, -7],
]
print(Solution().maxSumRetangle(a))
