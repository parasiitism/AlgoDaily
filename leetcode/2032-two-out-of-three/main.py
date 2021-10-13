from collections import *
"""
    1st: hashtable 

    Time    O(2*(A+B+C)) worst
    Space   O(2*(A+B+C))
    72 ms, faster than 87.50%
"""


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        nums3Set = set(nums3)
        counter = Counter()
        for x in nums1Set:
            counter[x] += 1
        for x in nums2Set:
            counter[x] += 1
        for x in nums3Set:
            counter[x] += 1
        res = []
        for x in counter:
            if counter[x] >= 2:
                res.append(x)
        return res
