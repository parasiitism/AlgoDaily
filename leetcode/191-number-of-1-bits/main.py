"""
    1st approach: bit op
    - use x&1 to check the least significant bit
    - use x>>1 to divide the number by 2

    Time    O(logn)
    Space   O(1)
    12 ms, faster than 95.71%
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count
