"""
    1st: binary search

    Time    O(NlogM)    M=10^5
    Space   O(1)
    1932 ms, faster than 59.57% 
"""


class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:

        remain_ratio = 1 - loss/100

        left = 0
        right = 10**5
        while left + 1e-5 < right:
            mid = (left + right)/2

            poured = 0
            for b in buckets:
                if b >= mid:
                    poured += (b - mid) * remain_ratio
                else:
                    poured -= (mid - b)

            if poured >= 0:
                left = mid
            else:
                right = mid
        return left
