"""
	2nd approach: bottom-up DP, learned from others https://zhuanlan.zhihu.com/p/32980698
	e.g. [10,15,20,30]
	dp[0] = 10
	dp[1] = 15 to get here, we must step on this stair, therefore it is not min(10, 15) = 10
	dp[2] = 20 + min(dp[0], dp[1]) = 20 + 10 = 30
	dp[3] = 30 + min(dp[1], dp[2]) = 20 + 15 = 35
	dp[4] = 0  + min(dp[2], dp[3]) = 0  + 30 = 30

	Time 	O(n)
	Space	O(n) the dp array
	4ms beats 100%
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = (len(cost) + 1) * [0]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost) + 1):
            curCost = 0
            if i < len(cost):
                curCost = cost[i]
            dp[i] = min(dp[i-1], dp[i-2]) + curCost
        return dp[len(cost)]
