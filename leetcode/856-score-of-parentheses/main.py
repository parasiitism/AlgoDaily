"""
    1st approach: stack, learned from others

    e.g.
    [0, 0] after parsing (
    [0, 0, 0] after (
    [0, 1] after )
    [0, 1, 0] after (
    [0, 1, 0, 0] after (
    [0, 1, 1] after )
    [0, 3] after )
    [6] after )

    Time    O(n)
    Space   O(n)
"""


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                pop = stack.pop()
                if pop == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2*pop
        return stack[-1]
