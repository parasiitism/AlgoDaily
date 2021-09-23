"""
    1st: forward backward arrays

    Time    O(3N)
    Space   O(2N)
    1160 ms, faster than 40.00%
"""


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        forwardMaxs = n * [0]
        backwardMins = n * [2**32]

        fMax = 0
        for i in range(n):
            fMax = max(fMax, nums[i])
            forwardMaxs[i] = fMax

        bMin = 2**32
        for i in range(n-1, -1, -1):
            bMin = min(bMin, nums[i])
            backwardMins[i] = bMin

        res = 0
        for i in range(1, n-1):
            x = nums[i]
            if forwardMaxs[i-1] < x < backwardMins[i+1]:
                res += 2
            elif nums[i-1] < x < nums[i+1]:
                res += 1
        return res
