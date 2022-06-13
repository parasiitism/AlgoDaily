"""
    Sort
    - actually we don't care about the order of an array for 'subsequences'

    Time    O(NlogN)
    Space   O(1)
"""


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_val = nums[0]
        cut = 0
        for i in range(1, len(nums)):
            if nums[i] - k > min_val:
                cut += 1
                min_val = nums[i]
        return cut + 1
