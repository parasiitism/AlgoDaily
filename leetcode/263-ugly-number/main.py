import heapq

"""
    2nd approach: math % and /

    Time  O(3logN) log base are 2, 3, 5
    Space O(1)
    24 ms, faster than 99.51%
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return 0
        while num % 2 == 0:
            num /= 2
        if num == 1:
            return True

        while num % 3 == 0:
            num /= 3
        if num == 1:
            return True

        while num % 5 == 0:
            num /= 5
        if num == 1:
            return True

        return False
