from collections import *

"""
    1st: hashtable + sort

    Time    O(RC + NlogN)
    Space   O(RC)
    260 ms, faster than 100.00%
"""


class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        N = len(arrays)
        counter = Counter()
        for i in range(N):
            for x in arrays[i]:
                counter[x] += 1
        res = []
        for key in counter:
            if counter[key] == N:
                res.append(key)
        return sorted(res)
