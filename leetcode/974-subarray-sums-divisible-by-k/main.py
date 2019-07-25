"""
    1st approach: similar to zero sum subarray
    - if prefixSum[i]%K == prefixSum[j]%k, it means that A[i+1:j] is divisible by K

    ref:
    - https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217979/Pictured-Explanation-Python-O(n)-Clean-Solution-8-Lines!

    Time    O(n)
    Space   O(n)
    268 ms, faster than 94.01%
"""


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = 0
        pfsum = 0
        mod_map = {
            0: 1
        }
        for i in range(len(A)):
            pfsum += A[i]
            if pfsum % K in mod_map:
                val = mod_map[pfsum % K]
                result += val
                mod_map[pfsum % K] = val+1
            else:
                mod_map[pfsum % K] = 1
        return result
