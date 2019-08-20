"""
    1st approach: brute force

    Time    O(n)
    Space   O(1)
    LTE
"""


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        for i in range(len(A)):
            maxVal = A[i]
            for j in range(i, len(A)):
                maxVal = max(maxVal, A[j])
                if L <= maxVal <= R:
                    res += 1
        return res


"""
    2nd approach: dynamic programming, learned from others
    
    e.g.
    A = [2, 1, 4, 2, 3], L = 2, R = 3

    if A[i] < L
    For example, i = 1. We can only append A[i] to a valid sub-array ending with A[i-1] to create new sub-array. So we have dp[i] = dp[i-1] (for i > 0)

    if A[i] > R:
    For example, i = 2. No valid sub-array ending with A[i] exist. So we have dp[i] = 0.
    We also record the position of the invalid number 4 here as prev.

    if L <= A[i] <= R
    For example, i = 4. In this case any sub-array starts after the previous invalid number to A[i] (A[prev+1..i], A[prev+2..i]) is a new valid sub-array. So dp[i] += i - prev

    Finally the sum of the dp array is the solution.

    ref:
    - https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/117723/Python-standard-DP-solution-with-explanation

    Time    O(n)
    Space   O(1)
    308 ms, faster than 70.26%
"""


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        dp = len(A) * [0]
        prev = -1
        for i in range(len(A)):
            if A[i] < L and i > 0:
                dp[i] = dp[i-1]
            if A[i] > R:
                prev = i
            if L <= A[i] <= R:
                temp = i - prev
                dp[i] = temp
        return sum(dp)
