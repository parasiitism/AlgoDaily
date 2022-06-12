from collections import *

"""
    hashtable

    Time    O(N)
    Space   O(N)
    1432 ms, faster than 40.00%
"""


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        ht = defaultdict(int)
        for i in range(len(nums)):
            x = nums[i]
            ht[x] = i
        for val, after in operations:
            idx = ht[val]
            ht[after] = idx
            del ht[val]
        res = n * [0]
        for key in ht:
            idx = ht[key]
            res[idx] = key
        return res
