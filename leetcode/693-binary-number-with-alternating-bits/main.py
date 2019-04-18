"""
    questions to ask:
    - negative numbers?
    - single bit numbers? what should we return if input is either 0 or 1?
"""

"""
    1st approach:
    1. get the rightmost digit
    2. iterate from the 2nd digit and check if it is the same with the previous digit

    Time    O(logn) <- log base is 10
    Space   O(1)
    20 ms, faster than 76.48%
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # get the rightmost digit
        prev = n & 1
        n >>= 1
        # iterate from the 2nd digit and check if it is the same with the previous digit
        while n > 0:
            temp = n & 1
            if temp == prev:
                return False
            prev = temp
            n >>= 1
        return True
