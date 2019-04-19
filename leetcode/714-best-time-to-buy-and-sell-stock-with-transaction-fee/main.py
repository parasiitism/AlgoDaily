import sys

"""
    1st approach: dynamic programming
    - on each day, we might either have a stock or dont have any stock
    - calculate our gain in both cases
    - gain on each day is a sub-problem

    Time    O(n)
    Space   O(1)
    652 ms, faster than 32.85%
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -sys.maxsize
        for price in prices:
            # actually we dont need this temp variable
            # temp = hold
            # because if we sell and buy a stock on the same day, your total gain must be less than just hold
            # due to the transaction fee

            # remain the hold OR to buy: we need to spend cash to purchase the current stock and transaction fee
            hold = max(hold, cash-price-fee)
            # remain the cash OR to sell: cash out the hold + cur price = all the cash we have
            cash = max(cash, hold+price)
        return cash, hold


a = [1, 3, 2, 8, 4, 9]
b = 2
print(Solution().maxProfit(a, b))

a = [1, 3, 7, 5, 10, 3]
b = 3
print(Solution().maxProfit(a, b))
