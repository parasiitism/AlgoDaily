"""
    class DP

    Time    O(N)
    Space   O(N)
    1863 ms, faster than 100.00%
"""


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = n * [1]  # store the length at every idx
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        res = 0
        for i in range(n):
            res += dp[i]
        return res
