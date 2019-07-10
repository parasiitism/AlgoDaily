"""
    the easiest approach: similar to subsets

    ref:
    - https://www.educative.io/collection/page/5668639101419520/5633779737559040/5666387129270272

    Time    O(2^n)
    Space   O(2^n)
    must be LTE
"""


class Solution():

    def knapsack(self, prices, weights, capacity):
        return self.dfs(prices, weights, capacity, 0)

    def dfs(self, prices, weights, capacity, curIdx):
        if capacity <= 0 or curIdx >= len(prices):
            return 0
        profit1 = 0
        if weights[curIdx] <= capacity:
            profit1 = prices[curIdx] + \
                self.dfs(prices, weights, capacity-weights[curIdx], curIdx + 1)
        profit2 = self.dfs(prices, weights, capacity, curIdx + 1)
        return max(profit1, profit2)


s = Solution()

a = [5, 3, 10, 4]
b = [4, 2, 8, 8]
c = 10
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 6
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 7
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 10
print(s.knapsack(a, b, c))

print("-----")

"""
    1st approach: optimize the recursive approach with memoization
    - When we add the values from bottom, 
    if we see the same capacity on the same level, it means that they will have the same result in their subtree.
    - so we can use a hashtable to store the substree result and avoid redundant calculation if we see the same capacity on the same level again

    ref:
    - https://www.educative.io/collection/page/5668639101419520/5633779737559040/5666387129270272

    Time    O(NC) N: number of items, C: capacity
    Space   O(NC)
"""


class Solution():

    def knapsack(self, prices, weights, capacity):
        cache = {}
        return self.dfs(prices, weights, capacity, 0, cache)

    def dfs(self, prices, weights, capacity, curIdx, cache):
        if capacity <= 0 or curIdx >= len(prices):
            return 0
        key = (capacity, curIdx)
        if key in cache:
            print("where?", key, cache[key])
            return cache[key]
        # profit that if we include item at curIdx
        profit1 = 0
        if weights[curIdx] <= capacity:
            profit1 = prices[curIdx] + \
                self.dfs(prices, weights, capacity -
                         weights[curIdx], curIdx + 1, cache)
        # profit that if we exclude item at curIdx
        profit2 = self.dfs(prices, weights, capacity, curIdx + 1, cache)
        maxProfit = max(profit1, profit2)
        cache[key] = maxProfit
        return maxProfit


s = Solution()
a = [5, 3, 10, 4]
b = [4, 2, 8, 8]
c = 10
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 6
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 7
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 10
print(s.knapsack(a, b, c))

print("-----")


"""
    2nd approach: dp with 2d array
    - 2d array structure: row * col = prices * capacity
    - on each cell, the value is the max profit up to we considering from prices[0] to prices[i] with capacity(j)
    - dp[i][j] = max (dp[i-1][j], price[i] + dp[i-1][j-weight[i]])

    ref:
    - https://www.educative.io/collection/page/5668639101419520/5633779737559040/5666387129270272

    Time    O(NC) N: number of items, C: capacity
    Space   O(NC)
"""


class Solution():

    def knapsack(self, prices, weights, capacity):
        dp = []
        for _ in range(len(prices)):
            temp = (capacity+1) * [0]
            dp.append(temp)

        # first row: put the profit if prices[0] <= current capacity
        for i in range(capacity+1):
            if weights[0] <= i:
                dp[0][i] = prices[0]

        for i in range(1, len(prices)):
            for j in range(1, capacity+1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= j:
                    profit1 = prices[i] + dp[i - 1][j - weights[i]]
                # exclude the item
                profit2 = dp[i - 1][j]
                # take maximum
                dp[i][j] = max(profit1, profit2)
        return dp[-1][capacity]


s = Solution()
a = [5, 3, 10, 4]
b = [4, 2, 8, 8]
c = 10
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 6
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 7
print(s.knapsack(a, b, c))

a = [1, 6, 10, 16]
b = [1, 2, 3, 5]
c = 10
print(s.knapsack(a, b, c))

print("-----")

# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# ri = input()
# nums = ri.split()
# L, N = int(nums[0]), int(nums[1])
# # read N lines
# prices, weights = [], []
# for i in range(N):
#     ri = input()  # raw_input() for python2.7
#     nums = ri.split()
#     P, W = int(nums[0]), int(nums[1])
#     prices.append(P)
#     weights.append(W)
# print(s.knapsack(prices, weights, L))

# """
# 10 4
# 5 4
# 3 2
# 10 8
# 4 8
# """
