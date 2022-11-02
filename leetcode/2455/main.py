"""
    array

    Time    O(N)
    Space   O(N)
    181 ms, faster than 42.86%
"""


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        selected = [x for x in nums if x % 2 == 0 and x % 3 == 0]
        total = sum(selected)
        cnt = len(selected)
        if total == 0:
            return total
        return total // cnt
