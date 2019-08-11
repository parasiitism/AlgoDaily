"""
    1st approach: DP
    - clone and revert the input string
    - do longest common subsequence against the input string

    Time    O(n^2)
    Space   O(n^2)
    LTE
"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        A = s
        B = s[::-1]
        if len(A) == 0 or len(B) == 0:
            return 0
        dp = []
        for i in range(len(A)+1):
            dp.append((len(B)+1)*[0])
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return res
