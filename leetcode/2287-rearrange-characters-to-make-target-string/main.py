from collections import *


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ctr = Counter(s)
        signature = Counter(target)
        res = 2**32
        for c in signature:
            times = ctr[c] // signature[c]
            res = min(res, times)
        return res
