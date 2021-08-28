"""
    1st: hashtable
    - similar to leetcode325, 525, 560, 930

    Time    O(N)
    Space   O(N)
    2624 ms, faster than 100.00%
"""


class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pfs = 0
        seen = {0: -1}
        res = 0
        for i in range(n):
            diff = nums1[i] - nums2[i]
            pfs += diff
            if pfs in seen:
                res = max(res, i - seen[pfs])
            else:
                seen[pfs] = i
        return res
