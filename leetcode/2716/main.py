"""
    hashset
    - think twice, basically it is asking if we can removing all the redundant occurrence of a character

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        hs = set()
        for c in s:
            hs.add(c)
        return len(hs)
