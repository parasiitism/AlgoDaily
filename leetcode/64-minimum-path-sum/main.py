class Solution(object):
    def minPathSum(self, grid):
        """
        2nd approach: dynamic programming
        - dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        - https://leetcode.com/articles/minimum-path-sum/

        Time    O(m*n)
        Space   O(m*n)
        100 ms, faster than 31.04%
        12may2019
        """
        dp = []
        for i in range(len(grid)):
            temp = [0]*len(grid[i])
            dp.append(temp)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]


class Solution1(object):
    def minPathSum(self, grid):
        """
        3rd approach: optimize the 2nd approach
            - dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        - actually u just need the previous layer
            - https://leetcode.com/articles/minimum-path-sum/
        Time    O(m*n)
        Space   O(n)
        84 ms, faster than 48.14%
        12may2019
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        dp = []
        for i in range(len(grid[0])):
            dp.append(0)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = grid[i][j] + dp[j-1]
                elif j == 0:
                    dp[j] = grid[i][j] + dp[j]
                else:
                    dp[j] = grid[i][j] + min(dp[j-1], dp[j])
        return dp[-1]


print(Solution1().minPathSum([]))
print(Solution1().minPathSum([[]]))
print(Solution1().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution1().minPathSum([[1, 3, 1, 4], [1, 5, 1, 1], [4, 2, 1, 2]]))
