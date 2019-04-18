"""
    1st approach: bottom up recursion + hashtable(dynamic programming)
    - do /2 for even, -+1 for odd with recursions
    - the key point is to avoid duplicate computation by using a hashtable to cache the key

    Time    O(n) <= for each number, we just calculate once
    Space   O(n)
    20 ms, faster than 84.55%
"""


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        ht = {}
        return self.helper(n, ht)

    def helper(self, n, ht):
        # retrieve number of steps from the hashtable if n presents
        if n in ht:
            return ht[n]
        # base case
        if n == 1:
            return 0
        # even
        if n % 2 == 0:
            a = self.helper(n/2, ht) + 1
            ht[n] = a
            return a
        # odd
        a = self.helper(n-1, ht) + 1
        b = self.helper(n+1, ht) + 1
        c = min(a, b)
        ht[n] = c
        return c
