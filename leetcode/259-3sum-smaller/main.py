"""
    2nd approach: 2 pointers
	- e.g. [2,3,6,10], 10
	pair=0,3, sum = 12, diff=+2, right--
	pair=0,2, sum = 8, diff=-2, left++ => count++
	pair=1,2, sum = 9, diff=-1, cannot move any pointers => count++
	...

	Time		O(n^2)
	Space		O(1)
	104 ms, faster than 48.79%
"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            num = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur = num + nums[left] + nums[right]
                if cur < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res
