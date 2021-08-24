"""
    1st: math
    - clockwise or anti-clockwise

    Time    O(N)
    Space   O(1)
    36 ms, faster than 33.33%
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        prevIdx = 0
        for i in range(len(word)):
            c = word[i]
            idx = ord(c) - ord('a')
            diff1 = abs((idx + 26 - prevIdx) % 26)
            diff2 = abs((prevIdx - (idx + 26)) % 26)
            res += min(diff1, diff2) + 1
            prevIdx = idx
        return res
