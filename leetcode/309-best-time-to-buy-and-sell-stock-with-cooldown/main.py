import sys

"""
    1st approach: dynamic programming
    - similar to lc714, but there is one more state for rest

    hold: keep holding OR buy new stock when we rest
    cash: cash out the hold and add the current stock value = get all cash
    rest: keep resting OR keep the new cash to rest

    ref:
    - https://www.youtube.com/watch?v=oL6mRyTn56M
    - see ./idea.png

    Time    O(n)
    Space   O(1)
    40 ms, faster than 36.33%
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cash = 0
        hold = -sys.maxsize
        rest = 0
        for price in prices:
            oldHold, oldCash, OldRest = hold, cash, rest
            # remain the hold OR to buy: we need to spend cash to purchase the current stock
            hold = max(oldHold, rest-price)
            # to sell: cash out the hold + cur price = all the cash we have
            cash = oldHold+price
            # to rest: either the rest or the cash is the max value we are going to rest
            rest = max(OldRest, oldCash)
        # after the days, the max gain we have is either the gain when we rest or the cash we just made
        return max(rest, cash)


a = [1, 2, 3, 0, 2]
print(Solution().maxProfit(a))
