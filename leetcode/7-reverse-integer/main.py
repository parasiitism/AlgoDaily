"""
    
    16 ms, faster than 92.79%
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        s = str(x)
        rev = s[::-1]
        temp = int(rev) * sign
        if temp < -2**31 or temp > 2**31-1:
            return 0
        return temp
