"""
    1st approach: math
    - calculate the median
    - for each number, the diff to median is the way to minimize the moves to equal an array

    Time    O(nlogn)
    Space   O(1)
    52 ms, faster than 80.83%
"""


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort
        nums = sorted(nums)
        # find median
        n = len(nums)
        median = -1
        if n % 2 == 0:
            median = (nums[n/2-1] + nums[n/2]) / 2
        else:
            median = nums[n/2]
        # for each number, accumulate the diff to median
        count = 0
        for num in nums:
            count += abs(num - median)
        return count
