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


print(Solution().integerReplacement(7))
print(Solution().integerReplacement(8))
print(Solution().integerReplacement(190))
print(Solution().integerReplacement(2**31-1))

print("-------------------------")

"""
    1st approach: bottom up recursion + bit operation
    - whenever we see an even, we shift << the number until it reaches to an odd number, count the number of steps in the meanwhile
    - so when the remain is an odd number other than 1, we do recursion
    - compare the reuslts from the recursions, -1, +1, we return the result as count + min(recursion(n-1), recursion(n+1))
    - we dont necessarily to use a hashtable to avoid duplicate computations because bit operation takes O(logn) time which is fast enough

    Time    O(nlogm) <= for each number, we take logM to compuate the division
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
        if n in ht:
            return ht[n]
        if n == 1:
            return 0
        count = 0
        while n % 2 == 0:
            count += 1
            n >>= 1
        if n == 1:
            return count
        a = self.helper(n-1, ht) + 1
        b = self.helper(n+1, ht) + 1
        c = min(a, b)
        ht[n] = count + c
        return count + c


print(Solution().integerReplacement(7))
print(Solution().integerReplacement(8))
print(Solution().integerReplacement(190))
print(Solution().integerReplacement(2**31-1))
