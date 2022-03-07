"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    870 ms, faster than 17.06%
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cntr_s = self.countChars(s)
        cntr_t = self.countChars(t)
        total = sum(cntr_s) + sum(cntr_t)
        charsInCommon = 0
        for i in range(26):
            charsInCommon += min(cntr_s[i], cntr_t[i])
        return total - charsInCommon*2

    def countChars(self, s):
        res = 26 * [0]
        for c in s:
            idx = ord(c) - ord('a')
            res[idx] += 1
        return res
