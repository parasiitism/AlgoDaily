import sys

"""
    1st: sort, learned from others
    - very tricky question, i dont think it easy to come up with during an interview

    idea:
    - for every pair, if A[i] < A[j], we should
        - increase the smaller one, e.g. A[i] + K
        - decrease the bigger one, e.g. A[j] - K
    - in each iteration, find the boundaries by comparing the potentail peak and dip
        - potentialPeak = max(upper-K, A[i]+K)
        - potentialDip = min(lower+K, A[i+1]-K)
    - at the end of each iteration, update the result if necessary

    Time    O(nlogn)
    Space   O(1)
    132 ms, faster than 90.21%
"""


class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        lower = A[0]
        upper = A[-1]
        res = upper - lower
        for i in range(len(A)-1):
            potentialPeak = max(upper-K, A[i]+K)
            potentialDip = min(lower+K, A[i+1]-K)
            res = min(res, potentialPeak - potentialDip)
        return res
