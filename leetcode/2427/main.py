"""
    Math: factorization

    Time    O(sqrt(A) + sqrt(B))
    Space   O(sqrt(A) + sqrt(B))
    55 ms, faster than 16.67%
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        A = self.getFactors(a)
        B = self.getFactors(b)
        ctr = Counter(A+B)
        res = 0
        for x in ctr:
            c = ctr[x]
            if c == 2:
                res += 1
        return res

    def getFactors(self, n):
        smalls = []
        bigs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                if i*i == n:
                    smalls.append(i)
                else:
                    smalls.append(i)
                    bigs.append(n//i)
            i += 1
        return smalls + bigs[::-1]
