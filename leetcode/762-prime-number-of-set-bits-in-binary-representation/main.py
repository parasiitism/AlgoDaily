"""
    1st approach: bitop
    - use lc191
    - for each number from L to R inclusive, see if the number of set bits is a prime

    Time    O(n)
    Space   O(1)
    1060 ms, faster than 15.91%
"""


class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
        count = 0
        for i in range(L, R+1):
            temp = self.hammingWeight(i)
            if temp in primes:
                count += 1
        return count

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count
