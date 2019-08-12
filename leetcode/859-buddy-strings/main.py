from collections import *

"""
    1st approach: string + hashtable
    - clummsy logic LOL

    Time    O(n)
    Space   O(n)
    32 ms, faster than 19.67%
"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        ht = defaultdict(int)
        indeces = []
        maxCnt = 0
        for i in range(len(A)):
            ht[A[i]] += 1
            maxCnt = max(maxCnt, ht[A[i]])
            if A[i] != B[i]:
                indeces.append(i)
        if len(indeces) == 0:
            if maxCnt >= 2:
                return True
        if len(indeces) != 2:
            return False
        i, j = indeces[0], indeces[1]
        B_ = B[:i] + B[j] + B[i+1:j] + B[i] + B[j+1:]
        return A == B_
