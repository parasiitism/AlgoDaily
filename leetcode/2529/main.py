import bisect
"""
    1st: array

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for x in nums:
            if x < 0:
                neg += 1
            if x > 0:
                pos += 1
        return max(neg, pos)


"""
    2nd: binary search

    Time    O(logN)
    Space   O(1)
"""


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left = bisect.bisect_left(nums, 0)
        right = bisect.bisect_right(nums, 0)
        return max(left, n - right)
