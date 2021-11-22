"""
    1st: math

    Time    O(N)
    Space   O(1)
    44 ms, faster than 100.00%
"""


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        n = len(plants)
        cur = capacity
        for i in range(n):
            p = plants[i]
            if cur >= p:
                cur -= p
                res += 1
            else:
                res += i + i + 1
                cur = capacity - p
        return res
