"""
    3rd approach: Kadan's algorithm
    - idea similar to leetcode 53:maximum subarray
    - for each item, store the max&mix among itself, or extend the previous max&min with itself
      e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
    - the result is the largest dp[i]
    - see ./idea.jpeg

    Time	O(n)
    Space	O(n)
    56 ms, faster than 28.11%
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minP = sys.maxsize
        maxP = -sys.maxsize
        res = -sys.maxsize
        for num in nums:
            if num > 0:
                minP = min(minP*num, num)
                maxP = max(maxP*num, num)
            else:
                temp = minP
                minP = min(maxP*num, num)
                maxP = max(temp*num, num)
            res = max(res, maxP)
        return res
