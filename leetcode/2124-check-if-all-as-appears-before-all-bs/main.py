"""
    1st: string

    Time    O(N)
    Space   O(1)
    36 ms, faster than 70.00%
"""


class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i-1] == 'b' and s[i] == 'a':
                return False
        return True
