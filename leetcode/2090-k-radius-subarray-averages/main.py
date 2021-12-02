"""
    1st: sliding window

    Time    O(N)
    Space   O(N) the result
    1848 ms, faster than 100.00%
"""


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = n * [-1]
        windowSum = 0
        for i in range(n):
            windowSum += nums[i]
            if i > 2*k:
                windowSum -= nums[i-2*k-1]
            if i >= 2*k:
                res[i-k] = windowSum // (2*k + 1)
        return res
