from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def digitCount(self, s: str) -> bool:
        ctr = Counter([int(c) for c in s])
        for i in range(len(s)):
            c = s[i]
            if ctr[i] != int(c):
                return False
        return True
