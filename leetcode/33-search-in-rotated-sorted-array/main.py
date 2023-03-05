"""
    2nd approach: still binary search but refactor a bit for understanding

    Time	O(logn)
    Space	O(1)
    32 ms, faster than 51.03%
    9may2019
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if target < nums[mid]:
                if nums[left] <= target < nums[mid] or nums[left] > nums[mid]:
                    # either 2 conditions:
                    # - target is within the range
                    # - the part on the left is rotated
                    right = mid - 1
                else:
                    # otherwise search in another half
                    left = mid + 1
            elif target > nums[mid]:
                if nums[mid] < target <= nums[right] or nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return mid
        return -1

a = [4,5,6,7,0,1,2]
b = 0
print(Solution().search(a, b))

a = [4,5,6,7,0,1,2]
b = 3
print(Solution().search(a, b))