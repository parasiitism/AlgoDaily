"""
    1st approach: sort
    
    e.g. [3,2,1,2,1,7,7,9,9]

    sort it and it becomes
    [1, 1, 2, 2, 3, 7, 7, 9, 9]
       +1 +1 +2 +2    +1    +1   <- result
    [1, 2, 3, 4, 5, 7, 8, 9, 10] <- target

    result = +1 +1 +2 +2 +1 +1 = 8

    Time    O(nlogn)
    Space   O(n) the hashset
    308 ms, faster than 56.29%
"""


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        A = sorted(A)
        res = 0
        hs = set()
        hs.add(A[0])
        for i in range(1, len(A)):
            if A[i] in hs:
                targetValue = A[i-1] + 1
                res += targetValue - A[i]
                A[i] = targetValue
                hs.add(targetValue)
            else:
                hs.add(A[i])
        return res
