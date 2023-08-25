"""
    1st: sliding window
    - the cruz: forbidden[i].length <= 10
    - so we can just try all possibilities at every index

    Time    O(F + 10W)
    Space   O(F)
"""


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        hs = set(forbidden)
        res = 0
        j = 0
        for i in range(n):
            cur = ''
            for k in range(10):
                if i-k >= j:
                    cur = word[i-k] + cur
                    if cur in hs:
                        j = i-k+1
            res = max(res, i - j + 1)
        return res
