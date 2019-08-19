"""
    1st: binary search

    Time    O(2logn)
    Space   O(1)
    12ms beats 100%
"""


class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = self.lowerBsearch(nums, target)
        right = self.upperBsearch(nums, target)
        if left < 0 or left+1 > len(nums) or nums[left] != target:
            return False
        count = right - left
        return count > len(nums)//2

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
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
        return right
