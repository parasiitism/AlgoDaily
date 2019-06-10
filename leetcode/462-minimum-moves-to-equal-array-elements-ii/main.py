"""
    1st approach: math
    - find the median
    - for each number, the diff between num and median are the "steps"

    Time    O(nlogn)
    Space   O(1)
    52ms beats 82%
"""


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        median = -1
        if n % 2 == 0:
            median = (nums[n/2-1] + nums[n/2]) / 2
        else:
            median = nums[n/2]
        count = 0
        for num in nums:
            count += abs(num - median)
        return count
