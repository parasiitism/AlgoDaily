"""
    1st: binary search
    - sort the input array(nums)
    - a valid triangle can be identified when a + b > c
    - so for every pairs, binary search the upper bound for the third side of a triangle

    Time    O(N^2 * logN)
    Space   O(1)
    1500 ms, faster than 10.24%
"""


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                target = nums[i] + nums[j]
                idx = self.upperBsearch(nums, j, target-1)
                res += idx - 1 - j
        return res

    def upperBsearch(self, nums, j, target):
        left = j + 1
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right
