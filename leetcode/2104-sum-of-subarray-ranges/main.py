"""
    1st: brute force

    Time    O(N^2)
    Space   O(1)
    4044 ms, faster than 9.09%
"""


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            _max, _min = nums[i], nums[i]
            for j in range(i+1, n):
                _min = min(_min, nums[j])
                _max = max(_max, nums[j])
                res += _max - _min
        return res
