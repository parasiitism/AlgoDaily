"""
    1st approach: lower bound binary search

    Time    O(logn)
    Space   O(1)
    40 ms, faster than 45.55%
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
