"""
  Given that the input number of rows and columns are the same, rotate the matrix in-place
"""


class Solution(object):
    def rotate(self, matrix, clockwise):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        Time    O(n)
        Space   O(1) just swap+transpose in-place
        """
        if clockwise:
            self.transpose(matrix)
            self.swapCols(matrix)
        else:
            self.swapCols(matrix)
            self.transpose(matrix)

    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swapCols(self, matrix):
        for i in range(len(matrix)):
            n = len(matrix[0])-1
            for j in range(n):
                if n-j > j:
                    matrix[i][j], matrix[i][n-j] = matrix[i][n-j], matrix[i][j]


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
Solution().rotate(a, True)
print(a)

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
Solution().rotate(a, False)
print(a)
