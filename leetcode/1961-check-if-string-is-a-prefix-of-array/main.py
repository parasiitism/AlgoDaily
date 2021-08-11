"""
    1st: string

    Time    O(N)
    Space   O(N)
    36 ms, faster than 50.00%
"""


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ''
        for w in words:
            res += w
            if res == s:
                return True
        return False
