"""
    1st: dynamic programming(top down recursion + cache)

    Time    O(N)
    Space   O(N)
    2579 ms, faster than 80.00%
"""


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}

        def f(i):
            if i >= len(questions):
                return 0
            if i in cache:
                return cache[i]
            pick = f(i + questions[i][1] + 1) + questions[i][0]
            skip = f(i + 1)
            cache[i] = max(pick, skip)
            return cache[i]
        return f(0)


"""
    2nd: dynamic programming(bottom up iteration)

    Time    O(N)
    Space   O(N)
    2469 ms, faster than 80.00%
"""


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = {}
        for i in range(N-1, -1, -1):
            s, bp = questions[i]
            dp[i] = max(
                dp[i+1] if i+1 < N else 0,
                (dp[i+bp+1] if i+bp+1 < N else 0) + s
            )
        return dp[0]
