import math

"""
    1st approach: log

    Time    O(1)
    Space   O(1)
    72 ms, faster than 96.24%
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        temp = round(math.log(n, 3))
        return n == 3 ** temp
