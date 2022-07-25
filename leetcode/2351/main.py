"""
    hashtable

    Time    O(N)
    Space   O(N)
    26 ms, faster than 100.00%
"""


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hs = set()
        for c in s:
            if c in hs:
                return c
            hs.add(c)
        return ''
