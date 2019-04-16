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
        for arr in matrix:
            dp.append(len(matrix[0]) * [0])
        result = 0
        # for each cell, check if itself can complete a larger square
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[i][j] = min(
                        dp[i-1][j-1],
                        min(dp[i-1][j], dp[i][j-1])) + 1
                result = max(result, dp[i][j])
        # area of a square
        return result*result


a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(Solution().maximalSquare(a))

a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "0", "0"],
]
print(Solution().maximalSquare(a))
