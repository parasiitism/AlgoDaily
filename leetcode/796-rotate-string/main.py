"""
    1st approach:
    - rotate A to see if B appears

    Time    O(n)
    Space   O(1)
    12 ms, faster than 90.20%
"""


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) == len(B) and len(A) == 0:
            return True
        i = 0
        while i < len(A):
            A = A[1:] + A[0]
            if A == B:
                return True
            i += 1
        return False


"""
    2nd approach:
    - 2A must contain a rotated string

    Time    O(n)
    Space   O(1)
    12 ms, faster than 90.20%
"""


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        C = A + A
        return len(A) == len(B) and B in C
