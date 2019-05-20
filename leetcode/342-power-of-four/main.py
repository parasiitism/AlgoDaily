import math
"""
    1st approach: log

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
