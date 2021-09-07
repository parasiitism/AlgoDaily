from collections import *
from bisect import *

"""
    1st: hashtable + binary search

    Time    O(N^3logN)
    Space   O(N)
    216 ms, faster than 50.00%
"""


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ht = defaultdict(list)
        for i in range(n):
            ht[nums[i]].append(i)

        res = 0
        for a in range(n):
            for b in range(a+1, n):
                for c in range(b+1, n):
                    key = nums[a] + nums[b] + nums[c]
                    if key in ht:
                        indices = ht[key]
                        d = bisect_right(indices, c)
                        res += len(indices) - d
        return res
