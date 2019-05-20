"""
    1st approach: classic bit op

    Time    O(32)
    Space   O(1)
    20 ms, faster than 95.86%
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        one = False
        while n > 0:
            if n & 1 == 1:
                if one == True:
                    return False
                one = True
            n >>= 1
        return True
