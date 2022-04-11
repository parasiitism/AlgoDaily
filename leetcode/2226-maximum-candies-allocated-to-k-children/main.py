"""
    1st: binary search

    Time    O(NlogM)
    Space   O(1)
    3022 ms, faster than 12.18%
"""


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = 2**32
        while left < right:
            mid = (left + right) // 2

            # count the number of candies each student can get
            count = 0
            for c in candies:
                count += c // mid

            if count >= k:
                left = mid + 1
            else:
                right = mid
        return left - 1
