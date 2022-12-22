"""
    1st: hashtable

    Time    O(NS)
    Space   O(N)
"""


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ctr = Counter()
        res = 0
        for w in words:
            key = self.genSign(w)
            if key in ctr:
                res += ctr[key]
            ctr[key] += 1
        return res

    def genSign(self, s):
        cnts = 26 * [0]
        for c in s:
            idx = ord(c) - ord('a')
            cnts[idx] = 1
        return tuple(cnts)
