class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        minRow = 0
        maxCol = len(matrix[0])-1
        maxRow = len(matrix)-1
        minCol = 0

        res = []

        while minRow <= maxRow and minCol <= maxCol:
            # go right
            for i in range(minCol, maxCol+1):
                res.append(matrix[minRow][i])
            minRow += 1
            # go down
            for i in range(minRow, maxRow+1):
                res.append(matrix[i][maxCol])
            maxCol -= 1
            # go left
            # minRow has been +1 previously, so maxRow must be >= new minRow in order to traverse correctly
            if minRow <= maxRow:
                for i in range(maxCol, minCol-1, -1):
                    res.append(matrix[maxRow][i])
                maxRow -= 1
            # go up
            # minCol has been +1 previously, so maxCol must be >= new minRow in order to traverse correctly
            if minCol <= maxCol:
                for i in range(maxRow, minRow-1, -1):
                    res.append(matrix[i][minCol])
                minCol += 1
        return res


a = [
    [1, 2, 3]
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3],
    [4, 5, 6],
]
print(Solution().spiralOrder(a))

a = [
    [1],
    [2],
    [3],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(Solution().spiralOrder(a))
