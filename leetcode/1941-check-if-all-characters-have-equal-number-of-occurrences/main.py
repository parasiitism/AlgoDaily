from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(26)
    36 ms, faster than 66.67%
"""


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        hs = set()
        for key in counter:
            hs.add(counter[key])
        return len(hs) == 1
