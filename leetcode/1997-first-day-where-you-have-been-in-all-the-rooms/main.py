"""
    1st: dynamic programming
    - learned from others

    ref:
    - https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/discuss/1445156/C%2B%2B-DP
    - https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/discuss/1445212/Python3-DP-O(n)

    Time    O(N)
    Space   O(N)
    1180 ms, faster than 80.00%
"""


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        mod = 10**9+7
        n = len(nextVisit)
        dp = n * [0]
        for i in range(1, n):
            dp[i] = dp[i-1] + (dp[i-1] - dp[nextVisit[i-1]] + 1) + 1
            dp[i] %= mod
        return dp[-1]
