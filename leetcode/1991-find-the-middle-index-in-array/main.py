"""
    1st: prefix sum

    Time    O(N)
    Space   O(N)
    40 ms, faster than 71.43%
"""


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prefixSums = (n+2) * [0]
        for i in range(n):
            if prefixSums[i] * 2 == total - nums[i]:
                return i
            prefixSums[i+1] = prefixSums[i] + nums[i]
        return -1
