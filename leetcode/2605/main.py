"""
    Greedy

    Time    O(99)
    Space   O(A+B)
"""


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        A = set(nums1)
        B = set(nums2)
        for i in range(1, 100):
            if i < 10:
                if i in A and i in B:
                    return i
            else:
                L = i // 10
                R = i % 10
                if L in A and R in B:
                    return i
                if R in A and L in B:
                    return i
        return -1
