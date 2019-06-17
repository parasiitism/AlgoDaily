"""
    easier to understand: always look for the pivot point
    1. if the left most number is less than the right most number, the left most is the result
    2. if not, look for the pivot point with binary search

    Time    O(logn)
    Space   O(1)
    12 ms, faster than 100.00%
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
            # if no left most < right most, the minval is the left most number
            if nums[left] <= nums[right]:
                return nums[left]

            # binary search, always keep the mid
            mid = (left + right)//2
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid + 1


"""
    same thing
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right)/2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid


"""
    variation: find max
"""


class Solution(object):
    def findMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            # if no left most < right most, the minval is the left most number
            if nums[left] <= nums[right]:
                return nums[right]

            # binary search, always keep the mid
            mid = (left + right + 1)//2
            if nums[left] >= nums[mid]:
                right = mid - 1
            else:
                left = mid


a = [3, 4, 5, 1, 2]
print(Solution().findMax(a))

a = [5, 6, 0, 1, 2, 3, 4]
print(Solution().findMax(a))

a = [6, 0, 1, 2, 3, 4, 5]
print(Solution().findMax(a))

a = [2, 1]
print(Solution().findMax(a))

a = [1, 2]
print(Solution().findMax(a))

a = [1, 2, 3, 4, 5, 6]
print(Solution().findMax(a))
