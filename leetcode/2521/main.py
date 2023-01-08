"""
    1st: factorization

    Time    O(N sqrt(N))
    Space   O(number of primes <= 1000)
"""


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        hs = set()
        for x in nums:
            factors = self.getPrimeFactors(x)
            hs |= set(factors)
        return len(hs)

    def getPrimeFactors(self, n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
            else:
                i += 1
        if n > 1:
            factors.append(n)
        return factors
