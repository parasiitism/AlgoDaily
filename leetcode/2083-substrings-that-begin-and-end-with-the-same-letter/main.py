from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(26)
    168 ms, faster than 100.00%
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ht = Counter()
        res = 0
        for c in s:
            res += ht[c]
            res += 1
            ht[c] += 1
        return res
