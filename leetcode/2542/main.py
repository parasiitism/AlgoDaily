from heapq import *

"""
    1st: sort + minheap
    - iterate B from largest to smallest AND maintain a k-length maximum-sum subsequence of A
    - find the max sum(A subsequen) * max(B) through the iteration

    Time    O(Nlogk)
    Space   O(K)
"""


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = []
        for i in range(n):
            pairs.append((nums1[i], nums2[i]))
        pairs.sort(key=lambda ab: -ab[1])

        res = 0
        num_sum = 0
        minheap = []
        for i in range(n):
            a, b = pairs[i]
            heappush(minheap, a)
            num_sum += a
            if len(minheap) > k:
                num_sum -= heappop(minheap)
            if len(minheap) == k:
                res = max(res, num_sum * b)
        return res
