"""
    1st approach
	- 2 arrays to save if the row or col has zeros
    - traverse the matrix again to set zeros

	Time	O(2RC)
	Space	O(R+C)
	116 ms, faster than 52.73%
	16may2019
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        zeroRows = len(matrix) * [False]
        zeroCols = len(matrix[0]) * [False]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRows[i] = True
                    zeroCols[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if zeroRows[i] == True or zeroCols[j] == True:
                    matrix[i][j] = 0
