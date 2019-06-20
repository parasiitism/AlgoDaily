"""
    1st approach: dynamic programming, learned from others
    - consider A[i] + A[j] + i - j => A[i] + i + A[j] - j
    - always maintain the largest A[i] + i
    - in each iteration, see if the maintained A[i]+i cab form the largest sum with A[cur] - cur

    ref:
    - https://leetcode.com/problems/best-sightseeing-pair/discuss/260850/JavaC%2B%2BPython-One-Pass
    - https://blog.csdn.net/fuxuemingzhu/article/details/88778887

    TIme    O(n)
    Space   O(1)
    420 ms, faster than 96.70%
"""


class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        res = 0
        for j in range(1, len(A)):
            res = max(res, A[i] + i + A[j] - j)
            if A[j] + j > A[i] + i:
                i = j
        return res
