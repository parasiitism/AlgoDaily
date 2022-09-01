"""
    stack

    Time    O(N)
    Space   O(N)
    608 ms, faster than 14.29%
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
