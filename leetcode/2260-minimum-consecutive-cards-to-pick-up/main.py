from collections import *

"""
    Time    O(N)
    Space   O(N)
    1049 ms, faster than 42.86%
"""


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        ht = defaultdict(int)
        res = 2**32
        for i in range(n):
            c = cards[i]
            if c in ht:
                diff = i - ht[c] + 1
                res = min(res, diff)
            ht[c] = i
        if res == 2**32:
            return -1
        return res
