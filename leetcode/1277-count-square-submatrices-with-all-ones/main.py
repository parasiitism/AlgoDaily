"""
    1st: dynamic programming
    - similar to lc221

    ref: 
    - https://www.youtube.com/watch?v=NYeVhmWsWec

    Time    O(RC)
    Space   O(RC)
    564 ms, faster than 87.98%
"""


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        r, c = len(matrix), len(matrix[0])
        if r == 0 or c == 0:
            return 0

        dp = [c * [0] for _ in range(r)]

        result = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                result += dp[i][j]
        return result


s = Solution()

# 15
a = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 1],
]
print(s.countSquares(a))
