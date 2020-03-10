from typing import List

"""
    1st: dynamic programming?
    - learned from others
    - 

    ref:
    - https://leetcode.com/articles/wiggle-subsequence/

    Time    O(N^2)
    Space   O(2N)
    192 ms, faster than 12.78%
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        up = len(nums) * [0]
        down = len(nums) * [0]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        return 1 + max(up[-1], down[-1])


"""
    2nd: dynamic programming?
    - learned from others
    - see 1.png, 2.png

    ref:
    - https://leetcode.com/articles/wiggle-subsequence/

    Time    O(N)
    Space   O(2N)
    192 ms, faster than 12.78%
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        up = 1
        down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)
