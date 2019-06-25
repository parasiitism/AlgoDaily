import math
"""
    1st approach: log

    64 = 4^3
    3 = log(64)/log(4)

    Time    O(1)
    Space   O(1)
    72 ms, faster than 96.24%
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        temp = round(math.log(num, 4))
        return num == 4 ** temp


"""
    2nd approach: math
    - divide by 4 until mod != 0

    Time    O(logn)
    Space   O(1) 
    20 ms, faster than 80.70% 
"""


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4
        return True
