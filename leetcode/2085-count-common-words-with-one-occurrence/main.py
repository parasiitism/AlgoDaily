from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    64 ms, faster than 100.00%
"""


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ctr1 = Counter(words1)
        ctr2 = Counter(words2)
        res = 0
        for key1 in ctr1:
            if key1 in ctr2 and ctr1[key1] == 1 and ctr2[key1] == 1:
                res += 1
        return res
