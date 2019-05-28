"""
    1st approach: recursion
    - in each recursion, explore all the possibilities and you win if your opponent lose

    Time    O(2^n)
    Space   O(2^n)
    1888 ms, faster than 22.89%
"""


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False

        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                temp = s[:i] + '--' + s[i+2:]
                if self.canWin(temp) == False:
                    return True
        return False


"""
    2nd approach: recursion + memoization
    - in each recursion, explore all the possibilities and you win if your opponent lose
    - memorize the result for intermedia state to avoid redundant calculation

    Time    O(2^n)
    Space   O(2^n)
    64 ms, faster than 82.39%
"""


class Solution(object):

    def __init__(self):
        self.m = {}

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False

        if s in self.m:
            return self.m[s]

        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                temp = s[:i] + '--' + s[i+2:]
                if self.canWin(temp) == False:
                    self.m[s] = True
                    return True
        self.m[s] = False
        return False
