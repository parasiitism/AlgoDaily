"""
    1st approach: brute force LOL

    Time    O(MN)
    Space   O(1)
    164 ms, faster than 63.70%
"""


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        for j in range(len(A[0])):
            for i in range(1, len(A)):
                if A[i][j] < A[i-1][j]:
                    res += 1
                    break
        return res
