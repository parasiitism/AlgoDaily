"""
    1D dynamic programming
    - maximum subarray sum

    Time    O(N)
    Space   O(26)
"""


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        scores = {}
        for i in range(26):
            c = alphabets[i]
            scores[c] = i + 1
        for i in range(len(chars)):
            c = chars[i]
            scores[c] = vals[i]
        res = 0
        cur = 0
        for c in s:
            cur = max(cur+scores[c], scores[c])
            res = max(res, cur)
        return res
