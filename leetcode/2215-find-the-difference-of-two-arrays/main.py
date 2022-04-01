"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    282 ms, faster than 83.33%
"""


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hs1 = set(nums1)
        hs2 = set(nums2)
        res = [[], []]
        for x in hs1:
            if x not in hs2:
                res[0].append(x)
        for x in hs2:
            if x not in hs1:
                res[1].append(x)
        return res
