"""
    1st: sort
    - hinted from others
    - in the larger array, every number can only be decreased down to 1
    - in the smaller array, every number can only be increased up to 6
    - sort the diffs until the target_diff <= 0
    - if larger array with all ones > smaller array with all 6s, return -1

    ref:
    - https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/discuss/1085859/Python-O(nlogn)-(faster-than-100.00)-with-explanation

    Time    O(NlogN)
    Space   O(N)
    1248 ms, faster than 100.00%
"""


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = sum(nums1), sum(nums2)
        if A == B:
            return 0
        larger, smaller = None, None
        if A > B:
            larger, smaller = nums1, nums2
        else:
            smaller, larger = nums1, nums2

        larger_to_subtract = [x-1 for x in larger]
        smaller_to_add = [6-x for x in smaller]
        diffs = larger_to_subtract + smaller_to_add
        diffs.sort(key=lambda x: -x)

        target_offset = abs(A - B)
        res = 0
        for d in diffs:
            target_offset -= d
            res += 1
            if target_offset <= 0:
                return res
        return -1
