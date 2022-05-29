from collections import *

"""
    hashtable

    Time    O(N)
    Space   O(N)
    39 ms, faster than 50.00%
"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnter = Counter(s)
        cnt = cnter[letter]
        return cnt * 100 // len(s)
