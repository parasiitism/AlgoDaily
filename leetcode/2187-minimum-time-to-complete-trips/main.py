"""
    1st: binary search

    Time    O(DlogN)
    Space   O(1)
    5706 ms, faster than 15.10%
"""


class Solution:
    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        left = 1
        right = 2**64
        while left < right:
            mid = (left + right)//2

            total = 0
            for t in times:
                total += mid//t

            if totalTrips <= total:
                right = mid
            else:
                left = mid + 1
        return right
