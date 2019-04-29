import sys

"""
    1st approach: binary search
	- for each pair, we look for the remain
	e.g. [1,2,3,4,5] 10
	for pair 1,2, search 7 within [3,4,5]
	for pair 1,3, search 6 within [4,5]

	Time		O(n^2logn)
	Space		O(1)
	1552 ms, faster than 5.01%
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = sys.maxsize
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                remain = target - nums[i] - nums[j]
                # search from j+1
                idx = self.bSearchNearest(nums, j+1, remain)
                # update res if necessary
                if idx >= j+1 and idx < len(nums):
                    total = nums[i] + nums[j] + nums[idx]
                    if abs(total-target) < abs(res-target):
                        res = total
        return res

    def bSearchNearest(self, nums, start, target):
        left = start
        right = len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # checking
        if right < start:
            return start
        if left > len(nums)-1:
            return len(nums)-1
        # compare
        if abs(target-nums[right]) < abs(target-nums[left]):
            return right
        return left


a = [0, 1, 2]
b = 3
print(Solution().threeSumClosest(a, b))

a = [-1, 2, 1, -4]
b = 1
print(Solution().threeSumClosest(a, b))

a = [-1, 2, 1, -4, 3]
b = 1
print(Solution().threeSumClosest(a, b))

print("---")
