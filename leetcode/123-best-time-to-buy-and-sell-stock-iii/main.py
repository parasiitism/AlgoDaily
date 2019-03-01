class Solution(object):
    def maxProfit(self, prices):
        """
        1st approach:
        - use the algo from Best Time to Buy and Sell Stock I

        Time    O(n^2)
        Space   O(1)
        LTE
        """
        result = 0
        for i in range(len(prices)):
            left = self.maxProfitWithin(prices[:i])
            right = self.maxProfitWithin(prices[i:])
            if left + right > result:
                result = left + right
        return result

    def maxProfitWithin(self, prices):
        if len(prices) < 2:
            return 0
        bay = prices[0]
        diff = 0
        for price in prices:
            if price < bay:
                bay = price
            if price - bay > diff:
                diff = price - bay
        return diff


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([2, 4]))
print(Solution().maxProfit([2, 4, 1]))
print(Solution().maxProfit([2, 4, 1, 4]))
