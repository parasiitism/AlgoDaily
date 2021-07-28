from collections import *

"""
    1st: dynamic programming (recursion + hashtable)
    - for every substring, pick a point, split it
        - check if 2 parts, X and Y, can be scrambled
        - check if 2 parts, Y and X, can be scrambled

    ref:
    - https://www.youtube.com/watch?v=sETxfdHwxc0

    Time    O(2^N) worst
    Space   O(2^N)
    60 ms, faster than 67.19%
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return self.check(s1, s2, {})

    def check(self, s1, s2, ht):
        if s1 == s2:
            return True
        key = (s1, s2)
        if key in ht:
            return ht[key]

        if Counter(s1) != Counter(s2):
            ht[key] = False
            return ht[key]

        N = len(s1)
        for i in range(1, N):
            if self.check(s1[:i], s2[:i], ht) and self.check(s1[i:], s2[i:], ht):
                return True
            if self.check(s1[:i], s2[N-i:], ht) and self.check(s1[i:], s2[:N-i], ht):
                return True

        ht[key] = False
        return ht[key]
