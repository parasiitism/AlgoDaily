"""
    dynamic programming

    Time    O(hig)
    Space   O(high)
    954 ms, faster than 20.00%
"""
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        
        dp = {}
        def dfs(remain):
            if remain < 0:
                return 0
            elif remain == 0:
                return 1
            if remain in dp:
                return dp[remain]
            z = dfs(remain - zero)
            o = dfs(remain - one)
            dp[remain] = (z + o) % mod
            return dp[remain]
        dfs(high)
        
        return sum(dfs(i) for i in range(low, high+1)) % mod
