"""
    classic approach: dynamic programming
    
    ref: 
    https://www.youtube.com/watch?v=Pw6lrYANjz4

    Time    O(n^2k)
    Space   O(n)
    MLE
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or k < 1:
            return 0

        # dp array to store profit of each day
        profit = []
        for _ in range(k+1):
            profit.append(len(prices)*[0])

        res = -sys.maxsize
        for i in range(1, k+1):
            for j in range(1, len(prices)):
                # select the max from
                # 1. the profit of previous day
                # 2. the profit from previous transactions + the current stock
                prevDay = profit[i][j-1]
                maxFromPrevDeal = -sys.maxsize
                for l in range(j):
                    temp = -prices[l] + profit[i-1][l]
                    maxFromPrevDeal = max(maxFromPrevDeal, temp)
                profit[i][j] = max(prevDay, prices[j]+maxFromPrevDeal)
            # update
            res = max(res, profit[i][-1])
        return res
