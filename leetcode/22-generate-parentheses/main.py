class Solution(object):

    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        self.permuate("", 0, 2*n)
        return self.res

    def permuate(self, s, i, k):
        if i == k:
            if self.isValid(s):
                self.res.append(s)
            return
        self.permuate(s + "(", i+1, k)
        self.permuate(s + ")", i+1, k)

    def isValid(self, s):
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack = stack[:-1]
                else:
                    return False
        return len(stack) == 0


print(Solution().generateParenthesis(-1))
print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
