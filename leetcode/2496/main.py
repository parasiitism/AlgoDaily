"""
    try catch

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = -2**32
        for c in strs:
            try:
                x = int(c)
                res = max(res, x)
            except:
                res = max(res, len(c))
        return res
