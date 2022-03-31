"""
    1st: math
    - if no armor, the mininum heath is the sum
    - if 1 armor, the minimum health is the armor OR the max damage

    Time    O(N)
    Space   O(1)
    699 ms, faster than 100.00%
"""


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) - min(armor, max(damage)) + 1
