"""
    questions to ask:
    - in-place? yes
    - will there be an empty array? yes
"""


"""
    1st approach: 2 pointers
    - wap the values until we move all the zero to the back of the array
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # always points to the first zero
        slow = 0
        for i in range(len(nums)):
            # if the current number is not zero, swap with the value at slow
            if nums[i] != 0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1
