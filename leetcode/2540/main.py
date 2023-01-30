"""
    1s: hashtable

    Time    O(N)
    Space   O(N)
"""


from bisect import *


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set(nums2)
        for x in nums1:
            if x in seen:
                return x
        return -1


"""
    2nd: binary search

    Time    O(NlogN)
    Space   O(1)
"""


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for x in nums1:
            j = bisect_left(nums2, x)
            print(j)
            if j != -1 and nums2[j] == x:
                return x
        return -1
