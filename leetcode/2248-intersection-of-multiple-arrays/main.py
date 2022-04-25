from collections import *

"""
    hashtable

    Time    O(N)
    Space   O(N)
    103 ms, faster than 70.00%
"""


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ctr = Counter()
        for row in nums:
            for x in row:
                ctr[x] += 1
        res = []
        for key in ctr:
            if ctr[key] == len(nums):
                res.append(key)
        return sorted(res)
