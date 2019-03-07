"""
    1st approach:
    1. check if the result of removing of any character in s equals t
    2. check if the result of removing of any character in t equals s
    3. check if removing any same-positioned character in both s and t which makes them the same

    Time    O(S+T+min(S,T))
    Space   O(1)
    124 ms, faster than 5.18%
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        if s == t:
            return False
        # check remove s
        for i in range(len(s)):
            x = s[:i] + s[i+1:]
            if x == t:
                return True
        # check remove t
        for i in range(len(t)):
            x = t[:i] + t[i+1:]
            if x == s:
                return True
        # since we now check 'edit', both strings must have length
        if len(s) != len(t):
            return False
        # check remove s and remove t
        for i in range(len(s)):
            x = s[:i] + s[i+1:]
            y = t[:i] + t[i+1:]
            if x == y:
                return True
        return False
