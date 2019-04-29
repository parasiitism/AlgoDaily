"""
    2nd approach: 2 pointers

    Time	O(n)
    Space	O(1)
    52 ms, faster than 44.85%
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        left, right = 0, len(nums) - 1
        while left < right:
            cur = nums[left] + nums[right]
            if cur == target:
                return [left+1, right+1]
            elif cur > target:
                right -= 1
            else:
                left += 1
        return []
