"""
    1st approach: read column by column

    Time    O(rc)
    Space   O(rc)
    60 ms, faster than 49.05%
"""


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(A[0]) == 0:
            return []
        arr = []
        for j in range(len(A[0])):
            temp = []
            for i in range(len(A)):
                temp.append(A[i][j])
            arr.append(temp)
        return arr
