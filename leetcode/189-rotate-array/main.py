"""
    1st approach:
    - store an extra array after rotation
    - put the numbers back to the input

    Time    O(2n)
    Space   O(n)
    52 ms, faster than 56.66%
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = nums[n-k:] + nums[:n-k]
        for i in range(len(nums)):
            nums[i] = temp[i]


"""
    2nd approach: reverse the array

    e.g. [1,2,3,4,5,6,7], k=3

    reverse the whole
    [7,6,5,4,3,2,1]

    reverse the k front items
    [5,6,7,4,3,2,1]

    reverse the 2nd half
    [5,6,7,1,2,3,4]

    Time    O(3n)
    Space   O(1)
    52 ms, faster than 56.66%
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1 or k <= 0:
            return
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, left, right):
        i = left
        j = right
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
