from typing import List

"""
    1st: binary search

    Time    O(NlogN)
    Space   O(N)
    56 ms, faster than 87.50%
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        res = []
        for num in nums:
            idx = self.lowerBsearch(sortedNums, num)
            res.append(idx)
        return res

    def lowerBsearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
