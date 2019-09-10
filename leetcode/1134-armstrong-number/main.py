"""
    1st: math

    Time O(N)
    Space O(1)
    12 ms, faster than 88.47%
"""


class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        k = len(str(N))
        total = 0
        n = N
        while n > 0:
            digit = n % 10
            total += digit**k
            n /= 10
        return total == N
