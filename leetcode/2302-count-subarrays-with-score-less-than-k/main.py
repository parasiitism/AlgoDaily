"""
    2 pointers
    - variation of a classic problem: Count Subarrays With Sum Less Than K
    - similar to leetcode713

    Time    O(N)
    Space   O(1)
    1368 ms, faster than 100.00%
"""


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        L = 0
        for R in range(len(nums)):
            cur += nums[R]
            while cur * (R - L + 1) >= k:
                cur -= nums[L]
                L += 1
            res += R - L + 1
        return res
