"""
    prefix sum
    
    Time    O(3N)
    Space   O(3N) including the result
"""
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = n * [0]
        right_sum = n * [0]
        pfs = 0
        for i in range(n):
            left_sum[i] = pfs
            pfs += nums[i]
        pfs = 0
        for i in range(n-1,-1,-1):
            right_sum[i] = pfs
            pfs += nums[i]
        res = n * [0]
        for i in range(n):
            res[i] = abs(left_sum[i] - right_sum[i])
        return res