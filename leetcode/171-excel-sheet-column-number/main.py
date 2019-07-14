"""
    1st approach: math 26th-cimal
    - convert each character from A-Z to 1-26
    - multiply the previous sum

    Time    O(n)
    Space   O(n)
    24 ms, faster than 99.64%
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res = res*26 + ord(c) - ord('A') + 1
        return res
