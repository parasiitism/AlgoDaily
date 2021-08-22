"""
    1st: dynamic programming (top-down recursion + hashtable)

    Time    O(N)
    Space   O(3N)
    LTE
"""


class Solution(object):
    def countSpecialSubsequences(self, nums):
        ht = {}

        def dfs(i, prev):
            if i == len(nums):
                if prev == 2:
                    return 1
                return 0
            key = (i, prev)
            if key in ht:
                return ht[key]
            res = 0

            # if it can be extend
            if nums[i] == prev or nums[i] == prev + 1:
                res += dfs(i+1, nums[i])
            # no matter extendable or not, move forward
            res += dfs(i+1, prev)

            res %= 10**9 + 7
            ht[key] = res
            return res
        return dfs(0, -1)


"""
    2nd: dynamic programming (bottom-up)
    
    dp[0] = number of sequences end with 0
    dp[1] = number of sequences end with 1, e.g. [0,1], [0,0,0,1]
    dp[2] = number of sequences end with 2, e.g. [0,1,2], [0,0,1,1,1,1,2,2]

    it makes sense but not easy to come up with that:
    dp[0] += dp[0] + 1
    dp[1] += dp[0] + dp[1]
    dp[2] += dp[1] + dp[2]

    Time    O(N)
    Space   O(3)
    2088 ms, faster than 78.19%
"""


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for x in nums:
            if x == 0:
                dp[0] += dp[0] + 1
                dp[0] %= 10**9 + 7
            elif x == 1:
                dp[1] += dp[0] + dp[1]
                dp[1] %= 10**9 + 7
            elif x == 2:
                dp[2] += dp[1] + dp[2]
                dp[2] %= 10**9 + 7
        return dp[2]
