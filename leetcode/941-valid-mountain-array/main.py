"""
    1st approach: 2 pointers

    e.g. 1
    3, 4, 6, 5, 4
          ^
        left
        right
    left == right so a valid mountain

    e.g. 2
    3, 5, 6, 1, 2, 7, 4, 2, 1
          ^        ^
        left    right

    left != right so not a valid mountain

    e.g. 3
    3, 4, 5, 5, 5
          ^     ^
        left    right
    left != right so not a valid mountain

    e.g. 4
    3, 4, 5, 6, 7
                ^
                left
                right
    left == right but they are out of bound so not a valid mountain

    Time    O(2n)
    Space   O(1)
    180 ms, faster than 75.98%
"""


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        left = 0
        for i in range(len(A)-1):
            if A[i+1] <= A[i]:
                left = i
                break
        right = 0
        for i in range(len(A)-1, 0, -1):
            if A[i-1] <= A[i]:
                right = i
                break
        if left == right and left > 0 and right+1 < len(A):
            return True
        return False
