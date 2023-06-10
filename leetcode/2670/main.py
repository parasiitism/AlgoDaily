"""
    prefix sum, suffix sum, hashtable

    Time    O(2N)
    Space   O(N)
"""


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        backward = []
        seen = set()
        for i in range(len(nums)-1, -1, -1):
            backward.append(len(seen))
            seen.add(nums[i])
        backward = backward[::-1]
        seen = set()
        res = []
        for i in range(len(nums)):
            seen.add(nums[i])
            res.append(len(seen) - backward[i])
        return res
