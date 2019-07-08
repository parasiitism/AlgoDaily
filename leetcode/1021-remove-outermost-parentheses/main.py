"""
    1st approach: stack
    - similar to lc20
    - once the openCount == 0, the previous substring is a valid parentheses string
    - then we can just remove the outermost parentheses of that substring and put the remain part to the result

    Time    O(n)
    Space   O(n) result
    24 ms, faster than 97.56% 
"""


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        openCount = 0
        slow = -1
        res = ''
        for i in range(len(S)):
            c = S[i]
            if c == '(':
                if openCount == 0:
                    slow = i
                openCount += 1
            elif c == ')':
                openCount -= 1
                if openCount == 0:
                    sub = S[slow:i+1]
                    res += sub[1:-1]
        return res
