class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int

        1st approach: classic dynamic programming approach
        - https://www.youtube.com/watch?v=NYeVhmWsWec

        Time  O(r*c)
        Space O(r*c)
        104 ms, faster than 44.55% 
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        # create a dp array for caching the submatrices sizes
        dp = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[0])):
                temp.append(0)
            dp.append(temp)
        result = 0
        # for each cell, check if itself can complete a larger square
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[i][j] = min(
                        dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
                result = max(result, dp[i][j])
        # area of a square
        return result*result
