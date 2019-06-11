"""
    1st approach: binary search betweeen 1 and num, 1 <= x <= num

    Time    O(logn)
    Space   O(1)
    16 ms, faster than 92.52%
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        while left <= right:
            mid = (left + right)/2
            if mid*mid < num:
                left = mid + 1
            elif mid*mid > num:
                right = mid - 1
            else:
                return True
        return False
