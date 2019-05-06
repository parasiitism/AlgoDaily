"""
    1st attempt

    similar to lc556

    1. find the pivot point
    2. find the FURTHEST number which is a bit larger than the pivot in 2nd half
    3. swap the pivot and the number
    4. sort the 2nd half
    see idea.png
    time 	O(n+n)
    space 	O(1)
    beats 100%
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # find the pivot from the increasing sequence from the right
        pivot = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        # if not pivot, it means this permutation is the largest,
        # so the next permutation is the smallest permutation
        if pivot == -1:
            self.reverse(nums, 0, len(nums)-1)
            return
        # find the number to swap
        target = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[pivot]:
                target = i
                break
        # swap
        nums[pivot], nums[target] = nums[target], nums[pivot]
        # reverse the increasing sequence from the right
        self.reverse(nums, pivot+1, len(nums)-1)

    def reverse(self, nums, start, end):
        left = start
        right = end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
