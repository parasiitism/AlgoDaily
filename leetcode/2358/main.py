"""
    binary search

    Time    O(log10000)
    Space   O(1)
    959 ms, faster than 16.67%
"""


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        left = 0
        right = n + 1
        while left < right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if total <= n:
                left = mid + 1
            else:
                right = mid
        return left - 1
