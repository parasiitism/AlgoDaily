"""
    Time        O(N)
    Space       O(1)
    88 ms, faster than 12.50%
"""


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for w in words:
            if s.find(w) == 0:
                res += 1
        return res
