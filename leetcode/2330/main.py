"""
    2 pointers

    Time    O(N)
    Space   O(1)
    95 ms, faster than 17.65%
"""


class Solution:
    def makePalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        diff = 0
        while left < right:
            if s[left] != s[right]:
                diff += 1
            left += 1
            right -= 1
        return diff <= 2
