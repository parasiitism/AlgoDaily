"""
    1st: brain teaser, math
    - actually there are 2 possibilties
        - add the pattern[0] to the beginning of the text
        - add the pattern[1] to the end of the text
    - pick the 1 from count the subs

    Time    O(N)
    Space   O(N)
    709 ms, faster than 80.00%
"""


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a = pattern[0] + text
        b = text + pattern[1]
        return max(self.count_sub(a, pattern), self.count_sub(b, pattern))

    def count_sub(self, s, pattern):
        count_0 = 0
        res = 0
        for c in s:
            if c == pattern[0] and c == pattern[1]:
                res += count_0
                count_0 += 1
            elif c == pattern[0]:
                count_0 += 1
            elif c == pattern[1]:
                res += count_0
        return res
