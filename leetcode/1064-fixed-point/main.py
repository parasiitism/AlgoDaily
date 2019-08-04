"""
    1st approach: binary search

    Time    O(logn)
    Space   O(1)
    52 ms, faster than 40.70%
"""


class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right)//2
            if mid < A[mid]:
                right = mid - 1
            elif mid > A[mid]:
                left = mid + 1
            else:
                return mid
        return -1
