"""
    1st: dynamic programming
    - this is actually a follow up of coin change 2, with limited coins

    Time    O(target * types * average count)
    Space   O(target * types)
"""


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        cache = {}

        def dfs(i, target):
            if target == 0:
                return 1
            if i >= len(types) or target < 0:
                return 0
            key = (i, target)
            if key in cache:
                return cache[key]
            count_i, mark_i = types[i]
            total = 0
            for j in range(count_i+1):
                total += dfs(i+1, target - j*mark_i)
                total %= 10**9+7
            cache[key] = total
            return total
        return dfs(0, target)
