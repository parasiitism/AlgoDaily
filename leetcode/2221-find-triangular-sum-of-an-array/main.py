"""
    1st: array
    - very similar to the Pascal Triangle problem

    Time    O((N+1)*N/2)
    Space   O(N)
    3143 ms, faster than 82.42%
"""


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        _nums = nums[:]
        while len(_nums) > 1:
            n = len(_nums)
            clone = (n - 1) * [0]
            for i in range(n-1):
                clone[i] = (_nums[i] + _nums[i+1]) % 10
            _nums = clone
        return _nums[0]
