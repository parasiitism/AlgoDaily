import sys

"""
    1st approach: top-down dfs + hashtable

    Time    O(CA) C: number of coins, A: amount
    Space   O(A)
    2264 ms, faster than 5.01%
"""


class Solution(object):
    def coinChange(self, coins, amount):
        ht = {}
        steps = self.dfs(coins, amount, ht)
        if steps == 2**32:
            return -1
        return steps

    def dfs(self, coins, amount, seen):
        if amount == 0:
            return 0
        if amount < 0:
            return 2**32
        if amount in seen:
            return seen[amount]
        min_steps = 2**32
        for c in coins:
            remain = amount - c
            steps = self.dfs(coins, remain, seen) + 1
            min_steps = min(min_steps, steps)
        seen[amount] = min_steps
        return min_steps


print(Solution().coinChange([5], 5))
print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1, 7, 11, 13, 17], 152))
print(Solution().coinChange(
    [70, 177, 394, 428, 427, 437, 176, 145, 83, 370], 7582))
print("--------------------")

"""
    2nd: dp
    learned from others: bottom-up
    e.g. coins = [1,2,5], amount = 7
    f(0) = 0  so if f(100-100), it output 0+1=1
    f(1) = min(f0)) + 1
    f(2) = min(f(1), f(0)) + 1
    f(3) = min(f(2), f(1)) + 1
    f(4) = min(f(3), f(2)) + 1
    f(5) = min(f(4), f(3), f(0)) + 1
    f(6) = min(f(5), f(4), f(1)) + 1
    f(7) = min(f(6), f(5), f(2)) + 1
    

    Time    O(CA) C: number of coins, A: amount
    Space   O(A)
    1136 ms, faster than 78.70%
"""


class Solution(object):
    def coinChange(self, coins, amount):
        n = amount + 1
        dp = n * [2**32]
        dp[0] = 0
        coins.sort()
        for i in range(1, n):
            for c in coins:
                if i - c < 0:
                    continue
                temp = dp[i - c] + 1
                dp[i] = min(dp[i], temp)
        if dp[amount] == 2**32:
            return -1
        return dp[amount]


print(Solution().coinChange([5], 5))
print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1, 7, 11, 13, 17], 152))
print(Solution().coinChange(
    [70, 177, 394, 428, 427, 437, 176, 145, 83, 370], 7582))
print("--------------------")
