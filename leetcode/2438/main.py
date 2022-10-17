"""
    math
    - get the bit represetation of N
    - construct the result based on the query

    Time    O(N)
    Space   O(N)
    2708 ms, faster than 80.00%
"""


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = self.getPowers(n)
        res = []
        for s, e in queries:
            p = 1
            for i in range(s, e+1):
                p *= powers[i]
            p %= 10**9 + 7
            res.append(p)
        return res

    def getPowers(self, n):
        i = 0
        powers = []
        while n > 0:
            if n & 1 == 1:
                powers.append(2**i)
            n >>= 1
            i += 1
        return powers
