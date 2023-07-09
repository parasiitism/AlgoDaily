"""
    1st: greedy
    - for every adjacent pair, if S[i-1] != S[i-1], we either:
        - flip all the digits from start to i-1
        OR
        - flip all the digits from i to end

    
    Time    O(N)
    Space   O(1)
"""


class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(1, n):
            if s[i-1] != s[i]:
                res += min(i, n-i)
        return res
