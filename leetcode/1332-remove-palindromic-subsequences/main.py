"""
    1st: string
    - there are only 2 letters in the input string, so the max number removals = 2
    - it means if the input string is panlindrome, the max number removals = 1

    Time    O(N)
    Space   O(N)
    20 ms, faster than 97.55%
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[::-1] == s:
            return 1
        return 2
