"""
    1st approach:
    - compare the cur[1:] with the previous row

    Time    O(r*c)
    Space   O(r)
    76 ms, faster than 34.37%
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return True
        prev = matrix[0]
        for i in range(1, len(matrix)):
            arr = matrix[i][1:]
            for j in range(len(arr)):
                if prev[j] != arr[j]:
                    return False
            prev = matrix[i]
        return True


"""
    2nd approach:
    - traverse the matrix diagonally

    Time    O(r*c)
    Space   O(1)
    80 ms, faster than 26.98%
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return True

        for j in range(len(M[0])):
            i = 0
            _j = j
            prev = matrix[i][_j]
            while i < len(matrix) and _j < len(matrix[0]):
                if matrix[i][_j] != prev:
                    return False
                prev = matrix[i][_j]
                i += 1
                _j += 1

        for i in range(len(M)):
            _i = i
            j = 0
            prev = matrix[_i][j]
            while _i < len(matrix) and j < len(matrix[0]):
                if matrix[_i][j] != prev:
                    return False
                prev = matrix[_i][j]
                _i += 1
                j += 1

        return True
