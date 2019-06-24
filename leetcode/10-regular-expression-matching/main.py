"""
    learned from others: dynamic programming

    ref:
    - https://www.youtube.com/watch?v=l3hda49XcDE

    Time    O(SP)
    Space   O(SP)
    40 ms, faster than 81.24%
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == None or p == None:
            return False

        dp = []
        for i in range(len(s)+1):
            temp = (len(p) + 1) * [False]
            dp.append(temp)

        dp[0][0] = True

        # deal with patterns like a* or a*b* or a*b*c*
        for j in range(2, len(dp[0])):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        """
            Rules:
            '.' Matches any single character.
            '*' Matches zero or more of the preceding element.
        """
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    # 1. if the current character and current pattern are the same
                    # 2. or if the current pattern is .
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        # 1. consider .*
                        # 2. consider a* and aaaaa...
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[-1][-1]
