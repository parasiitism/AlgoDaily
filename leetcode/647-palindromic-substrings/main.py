"""
    naive approach:
    generate all the substrings and check

    Time    O(n^3)
    Space   O(1)
"""

"""
    1st approach: expand from center like lc5

    Time    O(N^2)
    Space   O(1)
    164 ms, faster than 64.96%
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            singleMiddle = self.countPalindromes(s, i, i)
            doubleMiddle = self.countPalindromes(s, i, i+1)
            res += singleMiddle + doubleMiddle
        return res

    def countPalindromes(self, s, L, R):
        if R >= len(s):
            return 0
        if s[L] != s[R]:
            return 0
        total = 1
        while L-1 >= 0 and R+1 < len(s) and s[L-1] == s[R+1]:
            total += 1
            L -= 1
            R += 1
        return total
