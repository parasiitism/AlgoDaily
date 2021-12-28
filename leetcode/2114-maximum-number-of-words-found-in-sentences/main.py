"""
    1st: string

    Time    O(N) N: all characters
    Space   O(1)
    44 ms, faster than 80.00%
"""


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = -1
        for s in sentences:
            words = s.split()
            res = max(res, len(words))
        return res
