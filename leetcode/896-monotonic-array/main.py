"""
    questions to ask:
    - will the sequence contain less than 2 items? yes
    - will the numbers in the sequence are the same? yes e.g. [1,1,1,1,1,1,1]
"""


"""
    1st approach:
    1. check the polarity of the array from the begining
    2. check if the sequence follows the polarity

    Time    O(n)
    Space   O(1)
    452 ms, faster than 29.08%
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2:
            return True

        isIncrease = True
        i = 1
        while i < len(A) and A[i] == A[i-1]:
            i += 1

        if i < len(A) and A[i] < A[i-1]:
            isIncrease = False

        for j in range(i+1, len(A)):
            if isIncrease == True:
                if A[j] < A[j-1]:
                    return False
            else:
                if A[j] > A[j-1]:
                    return False
        return True
