"""
    1st: stack
    - reversely traverse the input string
    - ignore the ':', pile up the stack with digits(+T/F sometimes)
    - whenever we see a '?'
        - if it is a 'T', pop the 2nd top item from the stack
        - if it is a 'F', pop the 1st top item from the stack
    - the result is the 1st top item from the stack after the iteration

    ref:
    - ./idea.png

    Time    O(n)
    Space   O(n)
    40 ms, faster than 79.17%
"""


class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        i = len(expression)-1
        while i >= 0:
            d = expression[i]
            if d == ':':
                pass
            elif d == '?':
                i -= 1
                prev = expression[i]
                if prev == 'T':
                    stack.pop(-2)
                else:
                    stack.pop()
            else:
                stack.append(d)
            i -= 1
        return stack[-1]


s = Solution()

a = 'T?2:3'
print(s.parseTernary(a))  # 2

a = 'F?1:T?4:5'
print(s.parseTernary(a))  # 4

a = 'T?T?T:5:3'
print(s.parseTernary(a))  # T

a = 'T?T?F:5:3'
print(s.parseTernary(a))  # F

a = 'T?F?F:5:3'
print(s.parseTernary(a))  # 5

print("-----")

a = 'F?F?F:5:3'
print(s.parseTernary(a))  # 3

a = 'F?T?F:5:3'
print(s.parseTernary(a))  # 3

a = 'T?F?T:5:3'
print(s.parseTernary(a))  # 5

a = "F?T:F?T?1:2:F?3:4"
print(s.parseTernary(a))  # 4
