"""
    2 arrays min max
    - precompute to record the non-increasing and non-decreasing sequences
    e.g.
            [2, 1, 1, 1, 3, 4, 1]
    non-inc  1  2  3  4  1  1  2
    non-dec  0  5  4  3  2  1  1
    ans            ^  ^

    Time    O(N)
    Space   O(N)
    992 ms, faster than 60.00%
"""


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        non_inc = n * [1]
        non_dec = n * [1]
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                non_inc[i] = non_inc[i-1] + 1
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                non_dec[i] = non_dec[i+1] + 1
        res = []
        for i in range(k, n - k):
            if non_inc[i-1] >= k and non_dec[i+1] >= k:
                res.append(i)
        return res
