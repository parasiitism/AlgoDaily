"""
    1st: Dynamic Programming(Knapsack, top-down recursion)

    Time    O(Budget * N)
    Space   O(Budget * N)
    5517 ms, faster than 21.57%
"""


class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        cache = []
        for _ in range(n):
            cache.append((budget+1) * [None])

        def dfs(i, remain):
            if i == n:
                return 0
            if cache[i][remain]:
                return cache[i][remain]
            # don't buy it
            not_buy = dfs(i+1, remain)
            # buy it
            buy = 0
            if remain >= present[i]:
                diff = future[i] - present[i]
                buy = dfs(i+1, remain - present[i]) + diff

            cache[i][remain] = max(buy, not_buy)
            return cache[i][remain]

        return dfs(0, budget)
