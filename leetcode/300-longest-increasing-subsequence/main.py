"""
    1st approach: dynamic programming

    ref: Longest Increasing Subsequence
    - https://www.youtube.com/watch?v=CE2b_-XfVDk

    Time    O(n^2)
    Space   O(n)
    1068 ms, faster than 12.81%
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = len(nums) * [1]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        res = 0
        for x in dp:
            res = max(res, x)
        return res
