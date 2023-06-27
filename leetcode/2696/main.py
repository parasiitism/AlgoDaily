"""
    1st: stack
    - similar to the classic parenthesis problem

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def minLength(self, s: str) -> int:
        ht = {
            'B': 'A',
            'D': 'C'
        }
        stack = []
        for c in s:
            if len(stack) > 0 and c in ht and stack[-1] == ht[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
