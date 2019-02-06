class Solution(object):
    def rotate(self, matrix, clockwise):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        Time    O(n)
        Space   O(n) allocation of the new array
        """
        if clockwise:
            return self.clockewise(matrix)
        return self.anticlockewise(matrix)

    def clockewise(self, matrix):
        result = []
        for i in range(len(matrix[0])):
            temp = []
            for j in reversed(range(len(matrix))):
                temp.append(matrix[j][i])
            result.append(temp)
        return result

    def anticlockewise(self, matrix):
        result = []
        for i in reversed(range(len(matrix[0]))):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            result.append(temp)
        return result


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
]
print(Solution().rotate(a, True))
print(Solution().rotate(a, False))
