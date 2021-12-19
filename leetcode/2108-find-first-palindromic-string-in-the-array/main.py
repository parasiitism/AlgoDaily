"""
    1st: string

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.isPalindrome(w):
                return w
        return ""

    def isPalindrome(self, s):
        _s = s[::-1]
        return s == _s
