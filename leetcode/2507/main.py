"""
    Math

    Time    O(N*sqrt(N))
    Space   O(sqrt(N))
"""


class Solution:
    def smallestValue(self, n: int) -> int:
        last = None
        while True:
            factors = self.get_prime_factors(n)
            if len(factors) == 1:
                return factors[0]
            n = sum(factors)
            if n == last:
                return n
            last = n

    def get_prime_factors(self, n):
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
