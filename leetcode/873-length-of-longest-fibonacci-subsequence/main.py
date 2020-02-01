from typing import List
from collections import defaultdict

"""
    1st: brute force
    1. put every number in a hashset
    2. for every starting pair, we try to find the fibonacci-like subsequence as long as possible

    Time    O(N^2logM) at most 43 terms in any Fibonacci-like subsequence that has maximum value <= 10^9
    Space   O(N)
    1700 ms, faster than 15.99%
"""


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        hs = set(A)
        res = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in hs:
                    x, y = y, x + y
                    length += 1
                res = max(res, length)
        return res if res >= 3 else 0


"""
    2nd: dynamic programming, bottom up with an 2D array AND 1 hashset
    1. iterate from the smallest pair
    2. we check if the remain, A[i] - A[j], is in the hashset, 
        if yes, since remain + A[j] = A[i], we can try to check if (remain, A[j]) in DP array 
        - if yes, accumulate the count by dp[(A[j], A[i])] = dp[(remain, A[j])] + 1
        - else, dp[(A[j], A[i])] = 3

    ref:
    - https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/discuss/152343/C%2B%2BJavaPython-Check-Pair

    Time    O(N^2)
    Space   O(N^2)
    588 ms, faster than 85.46%
"""


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        hs = set(A)
        dp = defaultdict(int)
        for i in range(len(A)):
            for j in range(i):
                remain = A[i] - A[j]  # remain + A[j] = A[i]
                if remain < A[j] and remain in hs:
                    key = (A[j], A[i])
                    if (remain, A[j]) in dp:
                        dp[key] = dp[(remain, A[j])] + 1
                    else:
                        dp[key] = 3
                    # dp[(A[j], A[i])] = dp.get((remain, A[j]), 2) + 1 # alternatively
        return max(dp.values() or [0])
