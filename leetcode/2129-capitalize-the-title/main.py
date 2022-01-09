"""
    1st: string

    Time    O(N)
    Space   O(N) <- ressult
    28 ms, faster than 100.00%
"""


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []
        words = title.split()
        for w in words:
            if len(w) <= 2:
                res.append(w.lower())
            else:
                res.append(w[0].upper() + w[1:].lower())
        return ' '.join(res)
