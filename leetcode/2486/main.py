"""
    2 pointers
    - find T in S from left to right, the result is number of characters in T remain untouched

    Time    O(S)
    Space   O(1)
    199 ms, faster than 50.98%
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i in range(len(s)):
            if j < len(t) and t[j] == s[i]:
                j += 1
        return len(t) - j
