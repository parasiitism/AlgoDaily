"""
    1st: dynamic programming
    - similar to leetcode1987

    Time    O(N)
    Space   O(26)
    84 ms, faster than 33.71%
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        dp = 26 * [0]
        for c in s:
            idx = ord(c) - ord('a')
            dp[idx] = (sum(dp) + 1) % mod
        return sum(dp) % mod
