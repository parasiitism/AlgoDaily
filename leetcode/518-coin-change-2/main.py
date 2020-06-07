"""
    2nd attempt: DP, learned from others
    - similar to lc377 but diff loop arrangement

	the idea is to divide the problem into subproblems:
	for each amount, calculate the number of different combinations using the result from smaller amount
	
	e.g.
	dp[amount] = dp[amount] + dp[amount-coin]
	dp[4] = 1 + dp[2]
	it means 4 can be came up with 1111 and the dp[2](the combination of 2), which is 11 and 2
	therefore
	dp[4] = 1 + 2 = 3
	see ./explanation.jpeg

    Time    O(N * A)
    Space   O(N)
    192 ms, faster than 46.52%
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = (amount+1)*[0]
        dp[0] = 1
        for i in range(len(coins)):
            coin = coins[i]
            for j in range(1, amount+1):
                if j - coin >= 0:
                    dp[j] += dp[j-coin]
        return dp[amount]
