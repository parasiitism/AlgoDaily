class Solution(object):
    def maxProfit(self, prices):
        """
        1st approach: increasing sequence
        - keep track of the last item if the sequence is increasing
        - if the sequence decrease, sum the last-bay to the result and update the bay and last with the current price

        Time    O(n)
        Space   O(1)
        24 ms, faster than 97.73% 
        """
        if len(prices) < 2:
            return 0
        last = prices[0]
        bay = prices[0]
        res = 0
        for i in range(len(prices)):
            price = prices[i]
            if price >= last:
                last = price
                if i + 1 == len(prices):
                    res += last - bay
            else:
                res += last - bay
                bay = price
                last = price
        return res


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 5, 4, 3]))
print(Solution().maxProfit([1, 3]))
print(Solution().maxProfit([3, 1]))
print(Solution().maxProfit([1]))
print(Solution().maxProfit([1]))
