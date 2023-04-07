"""
    binary search

    Time    O(Nlog(2**64))
    Space   O(1)
"""


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = 2**64
        while left < right:
            mid = (left + right)//2

            total_fixed_cars = 0
            for r in ranks:
                total_fixed_cars += int(math.sqrt(mid // r))

            if cars <= total_fixed_cars:
                right = mid
            else:
                left = mid + 1
        return left
