"""
    1st: naive dynamic programming

    Time    O(N^M)
    Space   O(N^M)
    LTE: 77 / 122 test cases passed.
"""


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        indices = n * [0]
        cache = {}
        return self.dfs(piles, k, indices, cache)

    def dfs(self, piles, k, indices, cache):
        if k == 0:
            return 0
        key = tuple(indices)
        if key in cache:
            return cache[key]
        res = 0
        for i in range(len(piles)):
            j = indices[i]
            if j >= len(piles[i]):
                continue

            _indices = indices[:]
            _indices[i] += 1

            x = self.dfs(piles, k-1, _indices, cache) + piles[i][j]
            res = max(res, x)
        cache[key] = res
        return res


"""
    2nd: better dynamic programming
    - caching the (pIdx, k) when we process every pile

    Time    O(NM)
    Space   O(NM)
    7476 ms, faster than 34.36%
"""


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        cache = {}

        def dp(pIdx, k):
            if pIdx == n:
                if k == 0:
                    return 0
                if k > 0:
                    return -(2**32)
            key = (pIdx, k)
            if key in cache:
                return cache[key]
            res = dp(pIdx + 1, k)
            wallet = 0
            for i in range(min(k, len(piles[pIdx]))):
                wallet += piles[pIdx][i]
                fromNextPile = dp(pIdx + 1, k - i - 1)
                res = max(res, fromNextPile + wallet)
            cache[key] = res
            return res

        return dp(0, k)
