"""
    1st: stack
    - very annoying cases

    Time    O(N)
    Space   O(N)
    1029 ms, faster than 33.33%
"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        stack = []
        res = 0
        for i in range(n):
            c = directions[i]
            if c == 'L':
                if len(stack) > 0:
                    if stack[-1] == 'S':
                        res += 1
                    elif stack[-1] == 'R':
                        stack.pop()
                        res += 2
                        # e.g. RRRRRRRL
                        while len(stack) > 0 and stack[-1] == 'R':
                            stack.pop()
                            res += 1
                        stack.append('S')

            elif c == 'S':
                if len(stack) > 0:
                    # e.g. RRRRRRS
                    while len(stack) > 0 and stack[-1] == 'R':
                        stack.pop()
                        res += 1
                stack.append('S')

            elif c == 'R':
                stack.append('R')

        return res
