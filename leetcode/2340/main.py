"""
    array
    - find the min and its idex
    - re-order the array
    - find the max and its idex
    - sum the indices

    Time    O(5N)
    Space   O(N)
    590 ms, faster than 100.00% 
"""


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        smallest = min(nums)
        largest = max(nums)
        smallest_idx = 2**32
        largest_idx = -(2**32)
        for i in range(n):
            x = nums[i]
            if x == smallest:
                smallest_idx = min(smallest_idx, i)
        nums = [nums[smallest_idx]] + \
            nums[:smallest_idx] + nums[smallest_idx+1:]
        for i in range(n):
            x = nums[i]
            if x == largest:
                largest_idx = max(largest_idx, i)
        return smallest_idx + n - 1 - largest_idx
