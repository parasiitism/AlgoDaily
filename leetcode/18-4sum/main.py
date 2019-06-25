"""
    2nd approach: 2 pointers
	1. sort the numbers to make sure that the key will be unique
	2. for each num[i] + num[j], use 2 pointers, from the front and from the end, to find the pairs which nums[i]+nums[j]+nums[start]+nums[end] sum up to target
	3. use a set to deduplicate

	Time	O(n^3)
	Space	O(n)
	892 ms, faster than 21.58%
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        hs = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp == target:
                        key = (nums[i], nums[j], nums[left], nums[right])
                        hs.add(key)
                        # want no duplicate, so narrow down the range from both ends
                        left += 1
                        right -= 1
                    elif temp < target:
                        left += 1
                    else:
                        right -= 1
        return hs
