"""
    math
    - actually the sum must be the same for both nums1 and nums2
    - actually all diffs should be %k == 0, we just need to count how many off them 

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if sum(nums1) != sum(nums2):
            return -1
        if tuple(nums1) == tuple(nums2):
            return 0
        if k == 0:
            return -1
        res = 0
        for i in range(len(nums1)):
            d = nums1[i] - nums2[i]
            if d > 0:
                if d % k != 0:
                    return -1
                res += d // k
        return res
