"""
    prefix sum
    
    Time    O(N)
    Space   O(1)
    1052 ms, faster than 50.00% 
"""


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pfs = 0
        sfs = sum(nums)
        minAvgDiff = 2**32
        res = -1
        for i in range(n):
            pfs += nums[i]
            sfs -= nums[i]
            a = pfs // (i+1)
            b = 2**32
            if n-i-1 > 0:
                b = sfs // (n-i-1)
            else:
                b = sfs
            diff = abs(a - b)
            if diff < minAvgDiff:
                minAvgDiff = diff
                res = i
        return res
