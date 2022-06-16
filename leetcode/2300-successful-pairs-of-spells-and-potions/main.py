"""
    binary search

    Time    O(PlogP + SlogP)
    Space   O(1)
    3267 ms, faster than 14.29%
"""


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for sp in spells:
            idx = self.lowerBsearch(potions, sp, success)
            res.append(len(potions) - idx)
        return res

    def lowerBsearch(self, nums, spell, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid] * spell:
                right = mid
            else:
                left = mid + 1
        return left
