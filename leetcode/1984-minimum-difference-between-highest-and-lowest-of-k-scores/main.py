"""
    1st: sliding window

    Time    O(N)
    Space   O(k)
    104 ms, faster than 45.45%
"""


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        window = nums[:k]  # can be optimized by using a deque
        res = window[-1] - window[0]
        for i in range(k, n):
            window.pop(0)
            window.append(nums[i])
            res = min(res, window[-1] - window[0])
        return res
