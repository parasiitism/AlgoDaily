"""
    1st: string

    Time    O(N)
    Space   O(N)
    60 ms, faster than 33.33%
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        rev_prefix = ''
        for i in range(len(word)):
            c = word[i]
            rev_prefix = c + rev_prefix
            if c == ch:
                return rev_prefix + word[i+1:]
        return word
