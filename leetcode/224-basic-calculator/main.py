"""
    2nd approach: suggested solution at https://leetcode.com/problems/basic-calculator/discuss/62361/Iterative-Java-solution-with-stack
	- use 1 stack
	- calculate the numbers on the same level
	- when we see (, put the intermediate result into a stack, and new calculation start from the (
	- when we see ), pop the add/minus the result with the last item in the stack

	Time	O(2n) the nested loop actually just runs one time
	Space O(n)
    136 ms, faster than 67.45%
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []
        # 1 means positive, -1 means negative
        # we declare it as an integer because we want to put the +- in the stack too
        sign = 1
        num = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                # construct a multi-digits number if any, e.g. "23" = 2*10+3 = 23
                j = i
                num = 0
                while j < len(s) and s[j].isdigit():
                    num = num*10 + int(s[j])
                    j += 1
                # sum up the intermediate result
                res += sign * num
                i = j
            elif s[i] == '+':
                # the next number will be using +
                sign = 1
                i += 1
            elif s[i] == '-':
                # the next number will be using -
                sign = -1
                i += 1
            elif s[i] == '(':
                # put the intermediate result(from the front) and sign into the stack
                stack.append(res)
                stack.append(sign)
                # since we have put the intermediate result in stack,
                # we can reset the things for calculation starting from this (
                res = 0
                sign = 1
                i += 1
            elif s[i] == ')':
                # last item is the sign we saved for calculation e.g. 1+(2+3) the 1st +
                sign = stack.pop()
                # previousLevelResult the intermediate result before this level, (xxx)
                previousLevelResult = stack.pop()
                # sign*res is the result within the current (xxx)
                res = previousLevelResult + sign * res
                i += 1
            else:
                i += 1
        return res


print(Solution().calculate("1 + 1"))
print(Solution().calculate(" 2-1 + 2 "))
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))

"""
    3rd approach: stack + recursion
    - its actually the simplied version of lc772, just without * and /

    Time	O(n*h)
	Space   O(n + h) the recursion tree
    4496 ms, faster than 5.01%
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        for c in s:
            arr.append(c)
        return self.helper(arr)

    def helper(self, arr):
        stack = []
        sign = '+'
        num = 0
        while len(arr) > 0:
            c = arr.pop(0)
            if c.isdigit():
                num = num*10 + int(c)
            if c == '(':
                num = self.helper(arr)
            if c == '+' or c == '-' or c == ')' or len(arr) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                sign = c
                num = 0
                if c == ')':
                    break
        return sum(stack)
