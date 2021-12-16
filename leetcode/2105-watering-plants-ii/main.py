"""
    1st: 2 pointers
    - alice from the left
    - bob from the right
    - refill if necessary

    Time    O(N)
    Space   O(1)
    848 ms, faster than 33.33%
"""


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        res = 0
        left, right = 0, n-1
        canA, canB = capacityA, capacityB
        while left < right:
            if canA < plants[left]:
                canA = capacityA
                res += 1
            if canB < plants[right]:
                canB = capacityB
                res += 1
            canA -= plants[left]
            canB -= plants[right]
            left += 1
            right -= 1
        if left == right:
            if canA >= canB:
                if canA < plants[left]:
                    res += 1
            else:
                if canB < plants[right]:
                    res += 1
        return res
