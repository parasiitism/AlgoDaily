"""
    dynamic programming

    Time    O(N)
    Space   O(N)
    748 ms, faster than 25.00%
"""


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        dp = n * [1]
        for i in range(1, n):
            prev = s[i-1]
            cur = s[i]
            if ord(cur) - ord(prev) == 1:
                dp[i] = dp[i-1] + 1
        return max(dp)
