"""
    1st approach: recursion
    - the logic is similar to lc227 but we also do recursion when we see an open parenthesis

    Time    O(n^2) because we have to find the correspondign closing parenthesis for recursion
    Space   O(n)
    188 ms, faster than 9.26%
"""


class Solution(object):
    def calculate(self, s):
        if len(s) == 0:
            return 0
        stack = []
        sign = '+'
        num = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)

            if c == '(':
                # do recursion
                end = self.findClosing(s[i:])
                num = self.calculate(s[i+1:i+end])
                i += end

            if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = c
                num = 0
            i += 1
        return sum(stack)

    def findClosing(self, s):
        pCnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                pCnt += 1
            elif s[i] == ')':
                pCnt -= 1
                if pCnt == 0:
                    return i


# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
print(Solution().calculate("1 + 1"))
print(Solution().calculate(" 6-4 / 2 "))
print(Solution().calculate("2*(5+5*2)/3+(6/2+8)"))
print(Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))
