"""
    1st approach: better brute force
    
    Time    O(n^2)
    Space   O(1)
    TLE
"""
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(A)):
            minV = A[i]
            res += A[i]
            for j in range(i+1, len(A)):
                minV = min(minV, A[j])
                res += minV
        return res%(10**9 + 7)