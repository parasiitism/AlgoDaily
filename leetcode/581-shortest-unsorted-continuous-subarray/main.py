"""
    1st approach:
	1. compare the nums with its sorted result
	2. 2 pointers to look for the boundaries

	Time	O(nlogn)
	Space	O(n)
	188 ms, faster than 61.94%
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)
        left = -1
        for i in range(len(nums)):
            if sortedNums[i] != nums[i]:
                left = i
                break
        if left == -1:
            return 0
        right = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if sortedNums[i] != nums[i]:
                right = i
                break
        return right - left + 1
