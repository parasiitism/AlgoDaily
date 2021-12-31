"""
    1st: greedy
    - learned from others
    - 2 passes
        - from left to right, regard every 0 as an open
        - from right to left, regard every 0 as a close

    ref:
    - https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1646610/Python3-greedy-2-pass

    Time    O(2N)
    Space   O(1)
    276 ms, faster than 87.50%
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        # from left to right, regard every 0 as an open
        opens = 0
        for i in range(n):
            c = s[i]
            loc = locked[i]
            if loc == '0' or c == '(':
                opens += 1
            elif c == ')':
                opens -= 1
            if opens < 0:
                return False
        # from right to left, regard every 0 as a close
        closes = 0
        for i in range(n-1, -1, -1):
            c = s[i]
            loc = locked[i]
            if loc == '0' or c == ')':
                closes += 1
            elif c == '(':
                closes -= 1
            if closes < 0:
                return False
        return True
