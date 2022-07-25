from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    49 ms, faster than 33.33%
"""


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ctr = Counter(suits)
        if len(ctr) == 1:
            return "Flush"
        ctr = Counter(ranks)
        for key in ctr:
            if ctr[key] >= 3:
                return "Three of a Kind"
        for key in ctr:
            if ctr[key] >= 2:
                return "Pair"
        return "High Card"
