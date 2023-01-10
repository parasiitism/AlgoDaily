"""
    Sieve of Eratosthenes
    - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    - https://www.youtube.com/watch?v=Lj_SzTGr-G4
"""


class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        primes = n * [True]
        primes[0] = False
        primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i] == False:
                continue
            for j in range(i*i, n, i):
                primes[j] = False
        res = [i for i in range(n) if primes[i]]
        return len(res)


print(Solution().countPrimes(10))
print(Solution().countPrimes(101))
