"""
    1st: greedy

    Time    O(N)
    Space   O(1)
    948 ms, faster than 11.11%
"""


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        _min, _min_idx = 2**32, -1
        _max, _max_idx = -(2**32), -1
        for i in range(n):
            x = nums[i]
            if x < _min:
                _min = x
                _min_idx = i
            if x > _max:
                _max = x
                _max_idx = i
        if _min == _max:
            return 1
        a = min(_min_idx, _max_idx) + (n - max(_min_idx, _max_idx)) + 1
        b = max(_min_idx, _max_idx) + 1
        c = n - min(_min_idx, _max_idx)
        return min(a, b, c)
