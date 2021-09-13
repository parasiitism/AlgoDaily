"""
    1st approach: better brute force
    
    Time    O(n^2)
    Space   O(1)
    TLE
"""


class Solution(object):
    def sumSubarrayMins(self, A):
        res = 0
        for i in range(len(A)):
            minV = A[i]
            res += A[i]
            for j in range(i+1, len(A)):
                minV = min(minV, A[j])
                res += minV
        return res % (10**9 + 7)


"""
    2nd: mono-increasing stack
    - learned from others
    
    ref:
    - https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step

    Time    O(N)
    Space   O(N)
    493 ms, faster than 65.53%
"""


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        res = 0
        stack = []  # mono-increasing
        A = [-(2**32)] + A + [-(2**32)]
        for i in range(len(A)):
            x = A[i]
            while len(stack) > 0 and x < A[stack[-1]]:
                j = stack.pop()
                # the crux: the number of times A[j] appears as the mininum
                # i - j             the diff from the current back to A[j]
                # j - stack[-1]     the diff from A[j] back to previous min
                res += A[j] * (i - j) * (j - stack[-1])
            stack.append(i)
        return res % (10**9 + 7)
