"""
    1st: hashtable
    - count the number fo each character
    - subtract the source from target, to get the diff

    Time    O(S+T)
    Space   O(S+T)
    364 ms, faster than 11.57%
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ht_t = 26 * [0]
        ht_s = 26 * [0]
        for c in t:
            idx = ord(c) - ord('a')
            ht_t[idx] += 1
        for c in s:
            idx = ord(c) - ord('a')
            ht_s[idx] += 1
        res = 0
        for i in range(26):
            res += max(ht_s[i] - ht_t[i], 0)
        return res
