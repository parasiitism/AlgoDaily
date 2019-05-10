"""
    easier to understand: always look for the pivot point
    1. if the left most number is less than the right most number, the left most is the result
    2. if not, look for the pivot point with binary search

    Time    O(logn) -> O(n)
    Space   O(1)
    40 ms, faster than 47.10%
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            
            # if left most == right most and they equal to each other, left increment
            while left < right and nums[left] == nums[right]:
                left += 1
            
            # if no left most < right most, the minval is the left most number
            if nums[left] <= nums[right]:
                return nums[left]
            
            # binary search, always keep the mid
            mid = (left + right)//2
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid + 1