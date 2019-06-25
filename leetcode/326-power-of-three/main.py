import math

"""
    1st approach: log

    81 = 3^4
    4 = log(81)/log(3)

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


"""
    2nd approach: math
    - divide by 3 until mod != 0

    Time    O(logn)
    Space   O(1) 
    20 ms, faster than 80.70% 
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3
        return True
