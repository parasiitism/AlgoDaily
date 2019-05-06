"""
    1st approach:

    Time    O(2logn)
    Space   O(1)
    76 ms, faster than 37.48%
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = self.lowerBsearch(nums, target)
        b = self.upperBsearch(nums, target)
        return [a, b]

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        # remember to check range
        if left < 0 or left+1 > len(nums):
            return -1
        # remember to check if nums[left/right] == target
        if nums[left] != target:
            return -1
        return left

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        targetIdx = left - 1
        # remember to check range
        if targetIdx < 0 or targetIdx+1 > len(nums):
            return -1
        # remember to check if nums[left/right] == target
        if nums[targetIdx] != target:
            return -1
        return targetIdx
