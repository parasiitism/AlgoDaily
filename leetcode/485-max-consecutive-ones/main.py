"""
    1st approach:
    1. for each num, count the number of consecutive ones
    2. after count, compare with the intermediate result
    3. the final intermediate result is the reuslt

    380ms beats 20.77%
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cur = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 1:
                cur += 1
            if num == 0 or i+1 == len(nums):
                res = max(res, cur)
                cur = 0
        return res
