from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    119 ms, faster than 23.53%
"""


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cntr = Counter()
        for i in range(len(nums)-1):
            cur = nums[i]
            nxt = nums[i+1]
            if cur == key:
                cntr[nxt] += 1
        k, v = cntr.most_common(1)[0]
        return k
