
import bisect

"""
    1st: brute force + binary search
    - generate all the primes from 2 to right
    - binary search the left-most prime >= left and iterate thru the primes and get the result
    
    Time    O(right)
    Space   O(primes)
    TLE     
"""


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.getPrimes(right+1)
        idx = bisect.bisect_left(primes, left)
        res = [-1, -1]
        min_diff = 2**32
        for i in range(idx+1, len(primes)):
            diff = primes[i] - primes[i-1]
            if diff < min_diff:
                min_diff = diff
                res = [primes[i-1], primes[i]]
        return res

    def getPrimes(self, n):
        if n < 2:
            return []
        primes = n * [True]
        primes[0] = False
        primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i] == False:
                continue
            for j in range(i*i, n, i):
                primes[j] = False
        return [i for i in range(n) if primes[i]]
