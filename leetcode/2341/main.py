from collections import *

"""
    hashtable

    Time    O(N)
    Space   O(N)
    58 ms, faster than 53.85%
"""


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        removed = 0
        remain = 0
        for key in ctr:
            cnt = ctr[key]
            removed += cnt // 2
            remain += cnt % 2
        return [removed, remain]
