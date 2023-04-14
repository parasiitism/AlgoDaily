"""
    greedy

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        zeros = 0
        res = 0
        cur = 0
        for i in range(n):
            x = int(s[i])
            if x == 0:
                if cur == 0:
                    zeros += 1
                else:
                    cur = 0
                    zeros = 1
            else:
                if zeros > 0:
                    zeros -= 1
                    cur += 2
                res = max(res, cur)
        return res
