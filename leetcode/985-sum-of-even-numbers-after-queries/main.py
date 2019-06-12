"""
    1st approach: math
    1. add all the evens
    2. for each query
        - we subtract A[i] from the evensum if it is even
        - we add val to A[i]
        - we add A[i] to the evensum if it is even

    Time    O(n)
    Space   O(n)
    456 ms, faster than 74.12%
"""


class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        evenSum = 0
        for x in A:
            if x % 2 == 0:
                evenSum += x

        for val, idx in queries:
            if A[idx] % 2 == 0:
                evenSum -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                evenSum += A[idx]
            res.append(evenSum)
        return res
