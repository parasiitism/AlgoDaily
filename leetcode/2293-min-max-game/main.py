"""
    1st: array

    Time    O(NlogN)
    Space   O(N)
    103 ms, faster than 33.33%
"""


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            n = len(nums)
            arr = []
            for i in range(0, n, 2):
                if i//2 % 2 == 0:
                    arr.append(min(nums[i], nums[i+1]))
                else:
                    arr.append(max(nums[i], nums[i+1]))
            nums = arr
        return nums[0]
