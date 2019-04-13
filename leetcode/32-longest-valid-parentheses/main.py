"""
    1st approach: brute force

    Time    O(n^3)
    Space   O(1)
    LTE
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if self.isValid(sub):
                    res = max(res, j-i+1)
        return res

    def isValid(self, s):
        if len(s) == 0:
            return True
        openCount = 0
        for c in s:
            if c == '(':
                openCount += 1
            else:
                if openCount == 0:
                    return False
                else:
                    openCount -= 1
        return openCount == 0


a = "(()"
print(Solution().longestValidParentheses(a))

a = ")()())"
print(Solution().longestValidParentheses(a))

a = ")(()())"
print(Solution().longestValidParentheses(a))

a = ")(()()))"
print(Solution().longestValidParentheses(a))

a = ")(()()))))(()()())"
print(Solution().longestValidParentheses(a))

a = "()(()"
print(Solution().longestValidParentheses(a))

print("---------------")


"""
    2nd approach: stack
    1. when we see an open parenthesis, we put the index of it onto the stack
    2. when we see a close parenthesis, we check if the last item on the stack is a open parenthesis
        if yes, we pop the stack and the diff = i-stack[-1] is the length of a valid balenced parentheses string
        if no, we push the curent index onto the stack
    3. we can get the global max by comparing with the diff when we pop the stack

    ref:
    https://www.youtube.com/watch?v=r0-zx5ejdq0

    Time    O(n)
    Space   O(n)
    44 ms, faster than 58.92%
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = [-1]
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack[-1] != -1:
                    idx = stack[-1]
                    if s[idx] == '(':
                        pop = stack.pop()
                        diff = i - stack[-1]
                        res = max(res, diff)
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        return res


a = "(()"
print(Solution().longestValidParentheses(a))

a = ")()())"
print(Solution().longestValidParentheses(a))

a = ")(()())"
print(Solution().longestValidParentheses(a))

a = ")(()()))"
print(Solution().longestValidParentheses(a))

a = ")(()()))))(()()())"
print(Solution().longestValidParentheses(a))

a = "()(()"
print(Solution().longestValidParentheses(a))
