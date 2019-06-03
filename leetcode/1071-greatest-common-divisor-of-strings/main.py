"""
    1st approach: string slicing
    - for every substring(starting from the front), see if we can slice the str1 and str2 until they become empty strings
    
    e.g.
    str1 = ABCABC
    str2 = ABC

    slicing A from the front fails becos strings are not empty after slicing
    str1 = BCABC
    str2 = BC

    slicing AB from the front fails becos strings are not empty after slicing
    str1 = CABC
    str2 = C

    slicing ABC from the front succeeds becos strings are empty after slicing
    str1 = ''
    str2 = ''
    YEAH

    Time    O(ABB)
    Space   O(min(A, B))
    80 ms, faster than 5.08%
"""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        gcm = ""
        for i in range(len(str2)):
            sub = str2[:i+1]
            A = str1
            B = str2
            while len(A) > 0 and len(B) > 0:
                if A[:i+1] == sub and B[:i+1] == sub:
                    A = A[i+1:]
                    B = B[i+1:]
                else:
                    break
            while len(A) > 0 and A[:i+1] == sub:
                A = A[i+1:]
            while len(B) > 0 and B[:i+1] == sub:
                B = B[i+1:]
            if len(A) == 0 and len(B) == 0:
                gcm = sub
        return gcm
